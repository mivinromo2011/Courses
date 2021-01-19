#!/usr/bin/env python3

import re
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65435        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            op=data.decode()
            N=re.split('[+/*-]{1}',op)
            O=op[int(re.search('[+*/-]{1}',op).start())]
            a=int(N[0])
            b=int(N[1])            
            if(O=='+'):
                res=str(a+b)
                conn.send(res.encode())
            elif(O=='-'):
                res=str(a-b)
                conn.send(res.encode())
            elif(O=='*'):
                res=str(a*b)
                conn.send(res.encode())
            elif(O=='/'):
                res=str(a/b)
                conn.send(res.encode())
            else:
                conn.send(b'Invalid Operation')
