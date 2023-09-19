import os
import csv

from firewall.rule_list import get_all_rules

"""
manages a collection of rule object.
"""

"""
create a check_packet method.
it must iterate through the rules and checks if
a packet matches any of the rules, returning the associated action
"""
def compare_rules(primary_rule: str, secondary_rules: list):
    result = []
    for rule in secondary_rules:
        if str(primary_rule).strip() == str(rule).strip():
            result.append(True)
        else:
            result.append(False)
    return any(result)

def check_packet(src_addr, dst_addr, src_port, dst_port):
    try:
        #Get all the rules as array and iterate thought them
        for rule in get_all_rules():
            # check for IP
            if compare_rules(rule[1], [src_addr, dst_addr, "any"]) and compare_rules(rule[3], [dst_addr,src_addr, "any"]):
                # check for port
                if compare_rules(rule[2], [src_port, "any", 0]) and compare_rules(rule[4], [dst_port, "any", 0]):
                    if rule[0] == True: 
                        return True
                    elif rule[0] == False or str(rule[0]).lower() == "disable":
                        continue
        return False
    except Exception as e:
        print(f"[ERR] Error: {e}")
        return False
