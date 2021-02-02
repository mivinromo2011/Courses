#!/usr/bin/env python3

import socket

ServerAddr='127.0.0.1'
ServerPort=65432


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ServerAddr,ServerPort))
    playing=True
    print("Connected with server")
    data = s.recv(1024)
    print(data.decode())
    while playing:    	
       	data = s.recv(1024)
    	print(data.decode())
    	i=input("Enter i: ")
    	j=input("Enter j: ")
    	s.sendall(i.encode())
    	s.sendall(j.encode())
    	move_result = s.recv(1024)
    	if move_result.decode()=="Failure":
    		print("The move is invalid!")
    		continue
    	else:
    		print("move Accepted!")
    		curr_b=s.recv(1024)
    		curr_b=curr_b.decode()
    		print("After Your Move: ")
    		print(curr_b)
    		oppo_move=s.recv(1024)
    		oppo_move=oppo_move.decode()
    		print("After Opponent's Move: ")
    		print(oppo_move)    		
    		curr_res=s.recv(1024)
    		if curr_res.decode()=="Continue":
    			continue
    		else:
    			print(curr_res.decode())
    			s.close()
