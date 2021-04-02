#!/usr/bin/env python3

import math
import os
import random
import re
import sys

def check(s):
    i=0
    n=len(s)
    while i<n//2:
        if s[i]!=s[n-i-1]:
            return False
        i=i+1
    return True

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if check(s):
        return -1
    else:
        i=0
        n=len(s)
        while(i<n//2):
            if s[i]==s[n-i-1]:
                i=i+1
            else:
                j=n-i-1
                p=s[i:j]
                if check(p):
                    return j
                else:
                    return i
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()