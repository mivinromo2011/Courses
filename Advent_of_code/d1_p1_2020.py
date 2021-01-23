#!/usr/bin/env python3

""" the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.r example, suppose your expense report contained the following:
1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579. """

import sys

f=open(str(sys.argv[1]))
fc=f.read()
N=fc.split()

for i in range(0,len(N)):
	N[i]=int(N[i])

N.sort()
s=0
e=len(N)-1
print(s,e)

while s!=e:
	print("Checking: ..... " + str(N[s]) + " and " + str(N[e]))
	if((N[e]+N[s])==2020):
		print("Passed!")
		res=N[e]*N[s]
		print(res)
		break
	elif((N[e]+N[s])>2020):
		e-=1
		continue
	else:
		s+=1
		continue