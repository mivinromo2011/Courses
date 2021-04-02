#!/usr/bin/env python3

def d(root,x,s,p):
    if root.val==x:
        return s,p
    else:
        if root.right==None and root.left==None:
            return -1,p
        elif root.right!=None and root.left==None:
            return d(root.right,x,s+1,root.val)
        elif root.right==None and root.left!=None:
            return d(root.left,x,s+1,root.val)
        else:
            p1,s1=d(root.right,x,s+1,root.val)
            p2,s2=d(root.left,x,s+1,root.val)
            if p1!=-1:
                return p1,s1
            if p2!=-1:
                return p2,s2
            return -1,p
            
class Solution:
                
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        s1,p1=d(root,x,0,-1)
        s2,p2=d(root,y,0,-1)
        if s1==s2 and p1!=p2:
            return True
        else:
            return False