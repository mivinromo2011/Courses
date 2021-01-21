#!/usr/bin/env python3

import sys

def find_common(sec,guess):
    comm=[value for value in sec if value in guess]
    return comm
secret,guess=map(str,sys.stdin.readline().split())
b=len(find_common(secret,guess))
a=0
for i in range(len(secret)):
    if(secret[i]==guess[i]):
        a+=1
print(a,"A",(int(b)-int(a)),"B")
