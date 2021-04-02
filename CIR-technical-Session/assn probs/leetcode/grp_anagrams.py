#!/usr/bin/env python3

def anagram(s):
    p=''.join(sorted(s))
    return p

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        # return s
        p=[None]*n
        m={}
        c=0
        for i in range(n):
            p[i]=anagram(strs[i])
            if p[i] not in m:
                m[p[i]]=c;
                c=c+1
        s=[[] for i in range(c)]
        for i in range(n):
            s[m[p[i]]].append(strs[i])
        return s