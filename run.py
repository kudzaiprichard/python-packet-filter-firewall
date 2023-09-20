import threading
import time
from firewall.firewall import *
from firewall.packet import *
from firewall.rule_list import *

def run():
    print("FIREWALL IS RUNNING......")
    try:
        rules = RuleList()
        rules.add_rule(False,'192.168.36.44', '57881', '93.184.221.240', '80')
        
        packet_manager = Packet(rules.get_all_rules())
        firewall = Firewall(packet_manager)

        while True:
            for _ in range(10):
                firewall.run()
                print(rules.get_all_rules())
                time.sleep(100)

    except KeyboardInterrupt:
        print("\nEXITING FIREWALL.....")
        exit(1)

run()