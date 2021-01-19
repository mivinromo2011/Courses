#!/usr/bin/env python3

import socket

ServerAddr='127.0.0.1'
ServerPort=65432
MyPort=65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ServerAddr,ServerPort))
    s.sendall(b'Hello, World!')
    data = s.recv(1024)

print('Received', repr(data))
