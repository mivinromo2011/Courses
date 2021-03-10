#!/usr/bin/env python3
#CB.EN.U4CSE18439
#Server-Side

import socket
import random
import os
from _thread import *
import threading

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 12345
TC = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(clientsocket, clientaddress):
    clientsocket.send(str.encode('Welcome to the Server\n'))
    running = 1
    guess_no = 0
    randnum = genRanNum
    while running:
        Input = clientsocket.recv(1024)
        Inputstring = guess.decode('ascii')
        print(Inputstring)
        guess = int(Inputstring.split()[1])
        guess_no += 1
        running = 1
        if (guess == randnum):
            rep = ("Correct\r\n")
            clientsocket.send(rep.encode('ascii'))
            running = 0
        else:
            val_diff = (randnum - guess)
            if val_diff < 0:
                rep = ("The number is too high\r")
            else:
                rep = ("The number is too low\r")
            clientsocket.send(rep.encode('ascii'))
        if(guess_no==8):
            rep = ("Failed to guess the number. The correct number is : ",randnum )
            clientsocket.send(rep.encode('ascii'))
            rep = ("Failed\r\n")
            clientsocket.send(rep.encode('ascii'))
            running = 0
    clientsocket.close()
    print("Connection closed.")
def genRanNum:
	return random.randrange(1, 20)
while True:
    (clientsocket, clientaddress) = ServerSocket.accept()
    print("Connection received from: ", clientaddress)
    threading.Thread(target=threaded_client, args=(clientsocket, clientaddress)).start()
    print("Connection passed to new thread. Returning to listening.")

ServerSocket.close()