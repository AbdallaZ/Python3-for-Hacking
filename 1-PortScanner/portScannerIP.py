# you need to supply ip <--- to add dns lookup in future
import socket
from IPy import IP

def scan_port(ipadd, port):
    try:
        sock = socket.socket()
        #the less the faster but not very accurate
        sock.setttimeout(0.5)
        sock.connect((ipadd, port))
        print("[+] Port " + str(port) + " is Open")
    except:
        print("[-] Port " + str(port) + "is Closed")

ipadd = input("[+] Enter IP to Scan: ")
# Port 1-65535
for port in range(1,65535):
    scan_port(ipadd,port)

