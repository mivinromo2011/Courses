#!/usr/bin/env python3

def solve(s):
    p=""
    for i in range(len(s)):
        if s[i]!='#':
            p=p+s[i]
        else:
            if len(p)>0:
                p=p[:-1]
    return p

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return solve(S)==solve(T)