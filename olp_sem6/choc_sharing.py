tc=int(input())
for i in range(tc,0,-1):
    n=int(input())
    lent,bre=map(int,input().split())
    chocobar=list(map(int,input().split()))
    for bar in chocobar:
        if bar%a==0:
            x=bar/lent
            bre=bre-x
        else:
            y=bar/bre
            lent-=y
    if (lent==0 or bre==0):
        print("Yes")
    else:
        print("No")