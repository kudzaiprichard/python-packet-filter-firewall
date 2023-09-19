import threading
import time
from firewall.core import bind_sockets
from firewall.firewall import check_packet 
from firewall.util import get_interfaces


##Test 
# print(check_packet("192.168.2.100", "100", 80, 90))
# print(check_packet("192.168.3.100", "10.0.0.100", 0, 0))

interfaces = get_interfaces()

if len(interfaces.items()) < 4:
    print("Not enough interfaces")
    exit()
    
for key, val in interfaces.items():
    tr = threading.Thread(target=bind_sockets,args=([key, val],), name=key)
    tr.setDaemon(True)
    tr.start()
print("FIREWALL IS RUNNING ")

try:
    while True:
        for _ in range(10):
            time.sleep(.2)
except KeyboardInterrupt:
    print("\nEXITING FIREWALL")
    exit(1)