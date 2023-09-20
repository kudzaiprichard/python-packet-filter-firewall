from scapy.all import IP, TCP, sniff
import logging    # first of all import the module


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
                    if (pkt[IP].src == rule[1] and pkt[IP].dst == rule[3]): 

                        if(True): #pkt[TCP].sport == rule[2]  ports changes a lot
                            
                            #If they matches check if that rule is to be allowed or blocked
                            if rule[0] == True: 
                                log = "Status: ", "BLOCK", "Src IP: ",pkt[IP].src, "Src Port:", pkt[TCP].sport,"Dst IP: ", pkt[IP].dst,"Dst Port:" ,pkt[TCP].dport
                                logging.basicConfig(filename='firewall.log', filemode='w', format="%(asctime)s %(message)s")
                                logging.warning(log)
                                print(log)
                                
                            elif rule[0] == False:
                                log = "Status: ", "ALLOW", "Src IP: ",pkt[IP].src, "Src Port:", pkt[TCP].sport,"Dst IP: ", pkt[IP].dst,"Dst Port:" ,pkt[TCP].dport
                                logging.basicConfig(filename='firewall.log', filemode='w', format="%(asctime)s %(message)s")
                                logging.warning(log)
                                print(log)
                                
                    else:
                        print("Src IP: ",pkt[IP].src, "Src Port:", pkt[TCP].sport,"Dst IP: ", pkt[IP].dst,"Dst Port:" ,pkt[TCP].dport)     
            else:
                pass
                # return "Waiting for pkt...."
        except Exception as e:
            print(f"[ERR] Error could not get pkt: {e}")
            False

# capture = sniff(5)
# capture.summary()    
