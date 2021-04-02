#!/usr/bin/env python3

def solve(p,c):
    s=""
    if c==1:
        if p==4:
            s=s+"IV"
        elif p==9:
            s=s+"IX"
        else:
            if p>=5:
                s+='V'
                p=p-5
            while p>0:
                s=s+"I"
                p=p-1
            return s
    elif c==2:
        if p==4:
            s=s+"XL"
        elif p==9:
            s=s+"XC"
        else:
            if p>=5:
                s+='L'
                p=p-5
            while p>0:
                s=s+"X"
                p=p-1
            return s
    elif c==3:
        if p==4:
            s=s+"CD"
        elif p==9:
            s=s+"CM"
        else:
            if p>=5:
                s+='D'
                p=p-5
            while p>0:
                s=s+"C"
                p=p-1
            return s
    elif c==4:
        for i in range(p):
            s=s+"M"
        return s
    return s
            

def roman(n):
    s=""
    c=1
    while n>0:
        p=n%10
        t=str(solve(p,c))
        if len(t)>0:
            s=t+s
        c=c+1
        n=n//10
    return s

class Solution:
    def intToRoman(self, num: int) -> str:
        return roman(num)