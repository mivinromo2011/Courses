def getLargestString(s, k):
    # Write your code here
    count_a={x : s.count(x) for x in set(s)}
    n_removal=k//len(count_a)
    out=""
    out+=s[0]
    lk=1
    if(n_removal==0):
        for i in range (1,len(s)):
            if s[i]==s[i-1]:
                lk+=1
                if lk>k:
                    for j in count_a:
                        if j!=s[i] and count_a[j]!=0:
                            out+=j
                            count_a[j]-=1
                            break
                else:
                    out+=s[i]
            else:
                lk=1
                out+=s[i]
        if(all(value == 0 for value in count_a.values())):
            return(out)
        else:
            
print(getLargestString('azzz',2))