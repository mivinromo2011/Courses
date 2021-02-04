#!/usr/bin/env python3

n=int(input())
a=list()
b=list()
c=list()
for i in range(n):
	a.append(int(input()))

MAX=a[0]
b.append(MAX)
for i in range(1,n):
	MAX=max(MAX,a[i])
	b.append(MAX)
MAX=a[n-1]
c.insert(n-1,MAX)
#print(c,MAX)
for i in range(1,n):
	MAX=max(MAX,a[n-i-1])
	c.insert(0,MAX)
	print(c)
#print(c)
unit=0
for i in range(n):
	unit+=min(b[i],c[i])-a[i]

print(unit)