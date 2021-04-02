#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(b):
    a=[]
    s=[]
    for i in range(len(b)-2):
        if b[i]=='0' and b[i+1]=='1' and b[i+2]=='0':
            a.append(i)
    if len(a)==0:
        return 0
    i=1
    s.append(a[0])
    m=a[0]
    while i<len(a):
        if a[i]-m>2:
            s.append(a[i])
            m=a[i]
        i+=1
    return len(s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()