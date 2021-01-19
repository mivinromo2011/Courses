#!/usr/bin/env python3

import socket

ServerAddr='127.0.0.1'
ServerPort=65435
MyPort=65433
a=input("Enter First Element")
b=input("Enter Second Element")
c=input("Enter Operator")
N=a+c+b
#N.append(a)
#N.append(c)
#N.append(b)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ServerAddr,ServerPort))
    s.sendall(N.encode())
    data = s.recv(1024)

print('Received', repr(data.decode()))
