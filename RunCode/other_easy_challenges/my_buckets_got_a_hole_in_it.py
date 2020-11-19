#!/usr/bin/env python3

import sys

f=open(str(sys.argv[1]))
fc=f.read()
N=fc.split()

for i in range(0,len(N)):
	N[i]=int(N[i])

N.sort()


A=[0]*((N[-1]//10)+1)
for i in N:
	A[i//10]+=1


print(*A,sep='')