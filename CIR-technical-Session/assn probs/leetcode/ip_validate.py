#!/usr/bin/env python3

def zero(p):
    if (len(p)>1 and p[0]!='0') or len(p)==1:
        return False
    else:
        return True
    
def verify(p):
    s=int(p)
    if s<=255 and s>=0:
        return False
    else:
        return True
        
    
def number(p):
    a=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(p)):
        s=p[i]
        if s not in a:
            return True
    return False

def check(a):
    for i in range(len(a)):
        if a[i]=="":
            return False
        p=a[i]
        if number(a[i]) or zero(a[i]) or verify(a[i]):
            return False
    return True

def validate(a):
    for i in range(len(a)):
        if len(a[i])>4 or len(a[i])==0:
            return False
        for j in range(len(a[i])):
            p=int(ord(a[i][j]))
            if not ((((p >= 65 and p <= 70) or (p >= 97 and p <= 102))) or  (p >= 48 and p <= 57)):
                return False
    return True

class Solution:
    def validIPAddress(self, IP: str) -> str:
        four=list(map(str,IP.split('.')))
        six=list(map(str,IP.split(':')))
        if len(four)==4:
            if check(four):
                return "IPv4"
            else:
                return "Neither"
        elif len(six)==8:
            if validate(six):
                return "IPv6"
            else:
                return "Neither"
        else:
            return "Neither"