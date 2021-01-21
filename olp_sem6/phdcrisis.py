#!/usr/bin/env python3

N=int(input("Enter the No of Lines"))

while(N):
    problem=input()
    if problem=="P=NP":
        print("Skipped")
    else:
        print(int(problem[0])+int(problem[2]))
    N-=1
