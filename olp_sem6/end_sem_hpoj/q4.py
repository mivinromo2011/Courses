def solve(sol_work,n):
    var=0
    t_list=[]
    cnt=0
    sol_work.sort(key = lambda x: x[1],reverse=True)
    while(cnt<n):
        t_list.append(sol_work[cnt][1]+var)
        var+=sol_work[cnt][0]
        cnt+=1
    var=0
    for i in t_list:
        if i>var:
            var=i
    return var

tc=int(input())
for x in range(tc):
    sol_work=[]
    n=int(input())
    cnt=0
    while(cnt<n):
        brief,work=map(int,input().split())
        sol_work.append([brief,brief+work])
        cnt+=1
    soln=solve(sol_work,n)
    outp="Testcase"+str(x+1)+":"+str(soln)
    print(outp)
