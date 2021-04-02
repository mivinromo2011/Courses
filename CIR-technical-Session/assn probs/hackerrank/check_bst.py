#!/usr/bin/env python3

def max_solve(root):
    if root.left==None and root.right==None:
        return root.data 
    elif root.left==None and root.right!=None:
        r=max_solve(root.right)
        if r==-1:
            return -1
        if root.data<r:
            return max(root.data,r) 
        else:
            return -1
    elif root.right==None and root.left!=None:
        l=max_solve(root.left)
        if l==-1:
            return -1
        if root.data>l:
            return max(root.data,l) 
        else:
            return -1
    else:
        r=max_solve(root.right)
        l=max_solve(root.left)
        if l==-1 or r==-1:
            return -1
        if root.data>l and root.data<r:
            return max(root.data,max(l,r))
        else:
            return -1
        
def min_solve(root):
    if root.left==None and root.right==None:
        return root.data 
    elif root.left==None and root.right!=None:
        r=min_solve(root.right)
        if r==-1:
            return -1
        if root.data<r:
            return min(root.data,r) 
        else:
            return -1
    elif root.right==None and root.left!=None:
        l=min_solve(root.left)
        if l==-1:
            return -1
        if root.data>l:
            return min(root.data,l) 
        else:
            return -1
    else:
        r=min_solve(root.right)
        l=min_solve(root.left)
        if l==-1 or r==-1:
            return -1
        if root.data>l and root.data<r:
            return min(root.data,min(l,r))
        else:
            return -1
        
def check_binary_search_tree_(root):
    p1=max_solve(root)
    p2=min_solve(root)
    if p1==-1 or p2==-1:
        return False
    else:
        return True