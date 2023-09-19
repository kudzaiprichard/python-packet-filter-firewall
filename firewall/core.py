import socket
import time
import threading
from netaddr import IPNetwork
import psutil
import datetime
import logging
import ctypes, sys
from firewall.firewall import check_packet
from firewall.packet import ethernet_frame, ipv4_packet, tcp_packet, udp_packet
from firewall.util import PROTOCOLS

#The software should run with admin permissions
ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

logging.basicConfig(level=logging.INFO, filename="firewall.log", filemode="w")

# Create Send Socket for all the interfaces
send_sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
send_sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

def sendpacket(conn: socket.socket, payload, dst_ip):
    try:
        conn.sendto(payload, (dst_ip, 0))
    except PermissionError as broadcastError:
        print(broadcastError)
        pass
    except OSError as Error:
        print(Error)
        pass


def bind_sockets(interface):
    # create a socket connection to listen for packets
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW,socket.ntohs(0x0800))
    conn.bind((interface[0], 0))
    try:
        # continuously receive/listen for data
        while True:
            # send(bytes[, flags])
            raw_data, _ = conn.recvfrom(65536)
            """ 
            Create and gather the frame details from an ethernet instance
            """
            dest_mac, src_mac, eth_protocol, eth_data = ethernet_frame(raw_data)  # gather the frame details
            src_port, dst_port = 0, 0
            
            if eth_protocol == 8:
                s_addr, d_addr, protocol, ip_header = ipv4_packet(eth_data[14:34])
                logging.info(f"[{datetime.datetime.now()}] {interface[0]} ({d_addr}) >  {PROTOCOLS[protocol]}")
                if protocol == 6:
                    # Extract the TCP dst & src Ports
                    src_port, dst_port = tcp_packet(eth_data[34:54])

                elif protocol == 17:
                    # Extract the UDP dst & src Ports
                    src_port, dest_port, size, data = udp_packet(eth_data[34:42])
                    
                """ 
                All traffic is denied by default and only routes specified
                in the rules list are allowed 
                """
                if check_packet(s_addr, d_addr, src_port, dst_port):
                    sendpacket(send_sock, eth_data[14:], d_addr)
                else:
                    logging.error(f"<FAILED ROUTE>[{datetime.datetime.now()}] {interface[0]} ({s_addr}, {d_addr}) >  {PROTOCOLS[protocol]}")
    except KeyboardInterrupt:
        print("\n[END] STOPPED")
        return