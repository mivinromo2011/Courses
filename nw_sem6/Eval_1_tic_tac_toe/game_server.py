#!/usr/bin/env python3
#Server program

import socket
import random


move_list=[0,1,2]

def check_win(B):
	if(B[0][0]==B[0][1] and B[0][0]==B[0][2]):
		if(B[0][0]=="x"):
			return "p1"
		else:
			if(B[0][0]=="o"):
				return "p2"

	elif(B[0][0]==B[1][1] and B[0][0]==B[2][2]):
		if(B[0][0]=="x"):
			return "p1"
		else:
			if(B[0][0]=="o"):
				return "p2"
		
	elif(B[0][0]==B[1][0] and B[0][0]==B[1][2]):
		if(B[0][0]=="x"):
			return "p1"
		else:
			if(B[0][0]=="o"):
				return "p2"
		
	elif(B[1][0]==B[1][1] and B[1][0]==B[1][2]):
		if(B[1][0]=="x"):
			return "p1"
		else:
			if(B[1][0]=="o"):
				return "p2"
		
	elif(B[2][0]==B[2][1] and B[2][0]==B[2][2]):
		if(B[2][0]=="x"):
			return "p1"
		else:
			if(B[2][0]=="o"):
				return "p2"
		
	elif(B[0][1]==B[1][1] and B[0][1]==B[2][1]):
		if(B[0][1]=="x"):
			return "p1"
		else:
			if(B[0][1]=="o"):
				return "p2"
		
	elif(B[0][2]==B[1][2] and B[0][2]==B[2][2]):
		if(B[0][2]=="x"):
			return "p1"
		else:
			if(B[0][2]=="o"):
				return "p2"
		
	elif(B[0][2]==B[1][1] and B[0][2]==B[2][0]):
		if(B[0][2]=="x"):
			return "p1"
		else:
			if(B[0][2]=="o"):
				return "p2"
		
	else:
		return "n"

def check_filled(b):
	if b=="x" or b=="o":
		return 1
	else:
		return 0

def fill_board(B):
	for i in B:
		i="#"

def check_gameover(B):
	count=0
	for i in B:
		if i=="#":
			count+=1
	return count

def make_move(i,j,B,p):
	if(check_filled(B[i][j])):
		print("Place Occupied")
	else:
		print("Moving to "+"("+str(i)+str(j)+")")
		if p==1:
			B[i][j]="x"
		else:
			B[i][j]="o"

def print_board(B):
	for i in range(3):
		for j in range(3):
			print(B[i][j]+" |",end=" ")
		print("\n")

B=[["#"]*3]*3
print("Game Initialised Waiting for another player")
print("The Board: ")
print_board(B)

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
    	print("Connection established by another player")
    	msg="You are connected let us begin"
    	conn.sendall(msg.encode())
    	c=check_gameover(B)
    	while(True):
        	conn.sendall(b'Enter the move: ')
        	data = conn.recv(1024)
        	i=int(data.decode()) #Getting Player input1
        	data = conn.recv(1024)
        	j=int(data.decode()) #getting Player input2
        	if check_filled(B[i][j]): #Checking whether move is valid
        		msg="Failure"
        		conn.sendall(msg.encode())
        		continue
        	else:
        		make_move(i,j,B,1)
        		msg="Success" #Successfully completed a move
        		conn.sendall(msg.encode())
        		msg=print_board(B)
        		conn.sendall(msg.encode()) #Sending board view to the player
        		if (check_win(B)=="p1"): #Winner or Looser
        			msg="You Won!"
        			conn.sendall(msg.encode())
        		elif (check_win(B)=="p2"):
        			msg="You Lost! I won"
        			conn.sendall(msg.encode())
        		else: #make server move
        			pc_move=True
        			while pc_move:
        				i=random.choice(move_list)
        				j=random.choice(move_list)
        				if check_filled(B[i][j]): #checking for valid move
        					continue
        				else:
        					make_move(i,j,B,2)
        					msg=print_board(B)
        					conn.sendall(msg.encode())
        			msg="Continue"
        			conn.sendall(msg.encode())
        	c=check_gameover(B)