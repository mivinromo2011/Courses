#palindrome index HackerRank

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    slist=s.split()
    i=0
    j=len(s)
    while i!=j:
    	if slist[i]!=slist[j]:
			if slist[j]==slist[i+1]:
				return i
			else:
				return j    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s = raw_input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()