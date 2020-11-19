#!/usr/bin/env python

import sys


f = open(str(sys.argv[1]))   # Opening the file mentioned as argument
fc = f.read()	#reading the contents of the file
print(fc)	# printing the content of the file