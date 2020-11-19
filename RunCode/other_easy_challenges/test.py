#!/usr/bin/env python

import sys

f=open(str(sys.argv[1]))
fc=f.read()
A=fc.split()
print(int(A[1])+1)