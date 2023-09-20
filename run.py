import threading
import time
from firewall.firewall import *
from firewall.packet import *
from firewall.rule_list import *

def run():
    print("FIREWALL IS RUNNING......")
    try:
        rules = RuleList()
        rules.add_rule(False,'192.168.36.205', '59770', '192.168.36.44', '443')
        rules.add_rule(True,'192.168.36.44', '60237', '209.197.3.8', '80')
        rules.add_rule(True,'192.168.36.44', '60181', '192.168.36.205', '53')
        
        packet_manager = Packet(rules.get_all_rules())
        firewall = Firewall(packet_manager)

        while True:
            for _ in range(10):
                firewall.run()
                time.sleep(100)

    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)

run()