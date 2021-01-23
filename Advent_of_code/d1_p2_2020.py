#!/usr/bin/env python3
"""The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?"""

import sys

f=open(str(sys.argv[1]))
fc=f.read()
N=fc.split()

for i in range(0,len(N)):
	N[i]=int(N[i])

N.sort()
s=0
e=len(N)-1
m=s+1
print(s,e)

while s!=e:
	print("Checking: ..... " + str(N[s]) + " and " + str(N[m]) +" and " + str(N[e]))
	if((N[e]+N[s])==2020):
		continue
	elif((N[e]+N[s])>2020):
		e-=1
		continue
	else:
		
		print("Passed!")
		res=N[e]*N[s]*N[m]
		print(res)
		break