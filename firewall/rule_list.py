from firewall.rule import Rule

class RuleList:
    __rules = [
        Rule(False, "52.148.95.157", "443", "192.168.8.103", "48060").get_rule(),
        Rule(False, "23.101.25.24,443", "111", "192.168.8.103", "36438").get_rule()
    ]
    
    def __init__(self):
        self.__rules
        

    def add_rule(self,allow, src_ip, src_port ,dest_ip, dest_port):
        self.__rules.append(Rule(allow, src_ip, src_port, dest_ip, dest_port).get_rule())
        return self.__rules

    ##Takes a list of rules as array
    def add_rules(self,rules):
        for rule in rules:
            self.__rules.append(Rule(rule[0], rule[1], rule[2], rule[3], rule[4]).get_rule())
        return self.__rules

    def get_all_rules(self):
        return self.__rules
