#!/usr/bin/env python3
import sys
import math

f=open(str(sys.argv[1]))
fc=f.read()
N=fc.split()

i=0
while(i<len(N)):
	if float(N[i])<0:
		d=math.ceil(float(N[i]))
	else:
		d=math.floor(float(N[i]))

	if float(N[i+1])<0:
		i+=2
		continue
	else:
		r=int(math.floor(float(N[i+1])))	

	for j in range(1,r):
		if j%float(N[i])==0:
			print(int(j))
	if r%float(N[i])==0:
		print(r)
	if i!=len(N)-2:
		print("")	
	i+=2