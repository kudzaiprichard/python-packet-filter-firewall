from rule import Rule

__rules = [
    Rule(False, "192.168.8.100", "0", "224.0.0.251", "0").get_rule(),
    Rule(False, "52.148.95.157", "443", "192.168.8.103", "48060").get_rule(),
    Rule(False, "23.101.25.24,443", "111", "192.168.8.103", "36438").get_rule(),
    Rule(True, "10.0.0.100", "0", "192.168.3.100", "0").get_rule(),
    Rule(True, "192.168.3.100", "0", "10.0.0.100", "0").get_rule()
]

def get_all_rules():
    return __rules