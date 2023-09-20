import os
import csv
from firewall.rule_list import RuleList
from firewall.rule import Rule
from firewall.packet import Packet
from scapy.all import IP, TCP, sniff

"""
manages a collection of rule object.
"""

"""
create a check_packet method.
it must iterate through the rules and checks if
a packet matches any of the rules, returning the associated action
"""

class Firewall:
    def __init__(self, packet_manager):
        self.packet_manager = packet_manager
    
    def run(self):
        sniff(filter="ip",prn=self.packet_manager.get_summary)
