#!/bin/python3
import sys
import socket
from datetime import datetime as dt

#Defining our target
if len(sys.argv)==2:
    target=socket.gethostbyname(sys.argv[1]) #Translating hostname to IPV4

else:
    print("Invalid argument format")
    print("syntax: python3 portscanner.py <ip or hostname>")

#adding banner
print("-" *50)
print("Scanning Target" + target)
print("Start Time: "+ str(dt.now()))
print("-"*50)

try:
    for port in range(50,85):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target, port))  #error indicator
        if result == 0 :
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\n Keyboard interrupt")
    sys.exit()

except socket.gaierror:
    print("\n Hostname not resolved")
    sys.exit()

except socket.error:
    print("\n Couldn't connect to target")
    sys.exit()
