#!/usr/bin/env python3

def dfs(root,p,m,s):
    m[root.val]=p
    s[root.val]=root
    if root.right!=None:
        dfs(root.right,root.val,m,s)
    if root.left!=None:
        dfs(root.left,root.val,m,s)
        
def way(p,m):
    cur=p.val
    a=[]
    while cur!=-1:
        a.append(cur)
        cur=m[cur]
    return a

def ancestor(a,b):
    p=-1
    i=0
    while i<min(len(a),len(b)) and a[i]==b[i]:
        p=a[i]
        i=i+1
    return p

def r(a):
    s=[]
    n=len(a)
    i=n-1
    while i>=0:
        s.append(a[i])
        i=i-1
    return s
                
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        m={}
        s={}
        dfs(root,-1,m,s)
        a=way(p,m)
        b=way(q,m)
        a=r(a)
        b=r(b)
        ans=ancestor(a,b)
        return s[ans]