#!/usr/bin/env python3
#Server program

import socket

def check_win(B):
	if B[0][0]==B[0][1] and B[0][0]==B[0][2]:
		if B[0][0]=="x":
			return "p1"
		elif B[0][0]=="o":
			return "p2"
		else:
	elif B[0][0]==B[1][1] and B[0][0]==B[2][2]:
		if B[0][0]=="x":
			return "p1"
		elif B[0][0]=="o":
			return "p2"
		else:
	elif B[0][0]==B[1][0] and B[0][0]==B[1][2]:
		if B[0][0]=="x":
			return "p1"
		elif B[0][0]=="o":
			return "p2"
		else:
	elif B[1][0]==B[1][1] and B[1][0]==B[1][2]:
		if B[1][0]=="x":
			return "p1"
		elif B[1][0]=="o":
			return "p2"
		else:
	elif B[2][0]==B[2][1] and B[2][0]==B[2][2]:
		if B[2][0]=="x":
			return "p1"
		elif B[2][0]=="o":
			return "p2"
		else:
	elif B[0][1]==B[1][1] and B[0][1]==B[2][1]:
		if B[0][1]=="x":
			return "p1"
		elif B[0][1]=="o":
			return "p2"
		else:
	elif B[0][2]==B[1][2] and B[0][2]==B[2][2]:
		if B[0][2]=="x":
			return "p1"
		elif B[0][2]=="o":
			return "p2"
		else:
	elif B[0][2]==B[1][1] and B[0][2]==B[2][0]:
		if B[0][2]=="x":
			return "p1"
		elif B[0][2]=="o":
			return "p2"
		else:
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
		Print("Moving to "+"("+str(i)+str(j)+")")
		if p=1:
			B[i][j]="x"
		else:
			B[i][j]="o"

def print_board(B):
	for i in range(3):
		for j in range(3):
			print(B[i][j]+" | ")
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
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)