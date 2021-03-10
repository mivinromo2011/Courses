#!/usr/bin/env python3
#CB.EN.U4CSE18439
#Client-Side

import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 12345
print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))
Response = ClientSocket.recv(1024)
print(Response.decode('ascii'))
status = 1
while status:
    Input = input("Enter your guess: ")
    Inputstring = "Guess: " + str(Input) + "\r"
    ClientSocket.send(Inputstring.encode('ascii'))
    Response = ClientSocket.recv(1024).decode('ascii')
    print(Response)
    if (Response == "Correct\r\n" or Response == "Failed\r\n"):
        status = 0
ClientSocket.close()