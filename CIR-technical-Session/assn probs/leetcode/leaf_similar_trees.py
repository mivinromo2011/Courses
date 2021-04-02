def check(a,b):
    if len(a)!=len(b):
        return False
    else:
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True

def leaf(root,a):
    if root.right==None and root.left==None:
        a.append(root.val)
    if root.left!=None:
        leaf(root.left,a)
    if root.right!=None:
        leaf(root.right,a)
    
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        s1=[]
        s2=[]
        leaf(root1,s1)
        leaf(root2,s2)
        if check(s1,s2):
            return True
        else:
            return False