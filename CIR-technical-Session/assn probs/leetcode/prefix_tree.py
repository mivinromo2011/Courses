#!/usr/bin/env python3

class TrieNode:
    def __init__(self):
        self.m={}
        self.s={}
        
class Trie:
    def __init__(self):
        self.root=self.getNode()
        
    def getNode(self):
        return TrieNode()

    def insert(self, word: str) -> None:
        p=self.root
        for i in range(len(word)):
            k=""
            for j in range(i+1):
                k=k+word[j]
            p.m[k]=1
        p.s[word]=1
        
    def search(self, word: str) -> bool:
        p=self.root
        if word in p.s:
            return True
        else:
            return False
    
    def startsWith(self, prefix: str) -> bool:
        p=self.root
        if prefix in p.m:
            return True
        else:
            return False