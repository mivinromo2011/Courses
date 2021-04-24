import math

tc=int(input())
for i in range(tc,0,-1):
    ni=int(input())
    cod=[]
    for j in range(ni):
        ip=list(map(int,input().split()))
        cod.append(ip)
    dlen=0.0
    for k in range(1,ni):
        dlen+=math.sqrt(pow((cod[k][0]-cod[k-1][0]),2)+ pow((cod[k][1]-cod[k-1][1]),2))
    dlen+=math.sqrt(pow((cod[ni-1][0]-cod[0][0]),2)+ pow((cod[ni-1][1]-cod[0][1]),2))
    dlen=round(dlen,2)
    print(dlen)