"""
Each rule object should represent a firewall rule
specifying source IP, source and destination  IP,
and an action to either block it or allow it

The header of most packets contains details such as source and destination ports,
IP addresses, and protocol names. To apply packet filtering, we only need to know 
the source and destination IP addresses and ports.

A packet filtering rule contains the following fields:
Action - Can be either deny or allow.
Protocol - Name of transmission protocol, such as TCP.
SRC/DST IP - IP address of sender or receiver.
SRC/DST Port - Port of sender or receiver.
"""

class Rule:
    def __init__(self, allow, src_ip, src_port ,dest_ip, dest_port):
        self.allow = allow
        self.src_ip = src_ip
        self.src_port = src_port
        self.dest_ip = dest_ip
        self.dest_port = dest_port
    
    def get_rule(self):
        #returns an array 
        #['allow', ' 10.0.0.100', ' 0', ' 192.168.3.100', ' 0']
        return [self.allow, self.src_ip, self.src_port, self.dest_ip, self.dest_port]