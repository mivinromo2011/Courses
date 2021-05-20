def pcheck(n,ele,btree,pos):
    if 2*pos+1<n and btree[2*pos+1]>=0:
        pcheck(n,ele,btree,2*pos+1)
    if 2*pos+2<n and btree[2*pos+2]>=0:
        pcheck(n,ele,btree,2*pos+2)
    if btree[pos]==ele:
        if ( not(2*i+1<n and btree[2*pos+1]>=0) ) and (not(2*pos+2<n and btree[2*pos+2]>=0)):
            btree[pos]=-1

btree=list(map(str,input().split()))
bt_stack=[]
del_ele=int(input())
for i in range(len(btree)):
    if btree[i]=='null':
        bt_stack.append(-1)
    else:
        bt_stack.append(int(btree[i]))
pcheck(len(btree),del_ele,bt_stack,0)
while len(bt_stack)>0 and bt_stack[len(bt_stack)-1]==-1:
    bt_stack.pop()
for i in bt_stack:
    if i>=0:
        tmp=i
    else:
        tmp="null"
    print(tmp,end=" ")
