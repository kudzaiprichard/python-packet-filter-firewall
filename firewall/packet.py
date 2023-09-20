from scapy.all import IP, TCP, sniff

"""
Represents a network packet with source and destination IP addresses
"""
class Packet:
    def __init__(self,rules):
        self.rules = rules
    #True, "12.168.3.1009", "0", "10.0.0.100", "0"
    def get_summary(self, pkt):
        try:
            if TCP in pkt and IP in pkt:
                for rule in self.rules:
                    #print("src",pkt[IP].src, pkt[TCP].sport,"dst", pkt[IP].dst, pkt[TCP].dport)
                    #Check if the ip address and port number matches
                    if ( 
                        ( pkt[IP].src == rule[1]) or ( pkt[IP].dst == rule[3]) and
                        ( pkt[TCP].sport == rule[2]) or ( pkt[TCP].dport == rule[4])
                    ):
                        #If they matches check if that rule is to be allowed or blocked
                        if rule[0] == True: return "BLOCK", "src",pkt[IP].src, pkt[TCP].sport,"dst", pkt[IP].dst, pkt[TCP].dport
                        elif rule[0] == False: return "ALLOW", "src",pkt[IP].src, pkt[TCP].sport,"dst", pkt[IP].dst, pkt[TCP].dport
                    else:
                        return "src",pkt[IP].src, pkt[TCP].sport,"dst", pkt[IP].dst, pkt[TCP].dport    
            else:
                return "Waiting for pkt...."
        except Exception as e:
            print(f"[ERR] Error could not get pkt: {e}")
            False

# capture = sniff(5)
# capture.summary()    
# arr = [
#     [True, "192.168.36.44", "60916", "20.42.65.89", "443"], ##block
#     [True, "12.168.3.1009", "0", "10.0.0.100", "0"],
#     [True, "12.168.3.1009", "0", "10.0.0.100", "0"],
#     [False, "44.236.154.173", "443", "192.168.36.44", "61035"] ##allow
# ]        
# packet = Packet(arr)
# sniff(10,filter="ip",prn=packet.get_summary)

    #sniff(filter="ip",prn=get_summary)
    # or it possible to filter with filter parameter...!
    #sniff(filter="ip and host 192.168.0.1",prn=get_summary)