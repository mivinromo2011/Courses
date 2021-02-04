#!/usr/bin/env python3

prices=list()
span=[0]*7

for i in range(7):
	prices.append(int(input()))
	j=i
	while(j>=0):
		if(prices[i]>=prices[j]):
			span[i]+=1
			j-=1
		else:
			break
for i in span:
	print(i)