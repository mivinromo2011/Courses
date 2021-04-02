#include<iostream>
#include<bits/stdc++.h>
#include<algorithm>
#include<math.h>
#include<string.h>
using namespace std;
long long power(int a,long long b)
{
    if(b==0)
        return 1;
    long long p=power(a,b/2);
    p=p*p;
    if(b%2==1)
        p=p*a;
    return p;
}
string bin(long long n)
{
    string s="";
    while(n>0)
    {
        int k=n%2;
        s+=to_string(k);
        n/=2;
    }
    return s;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long t,n,c,i;
    string s;
    cin>>t;
    while(t--)
    {
        cin>>n;
        s=bin(n);
        n=s.length();
        c=0;
        for(i=0;i<n;i++)
            if(s[i]=='0')
                c+=power(2,i);
        cout<<c<<"\n";
    }
    return 0;
}