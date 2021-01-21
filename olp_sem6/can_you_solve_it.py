#!/usr/bin/env python3
  
def cDiff(i,j,arr): 
    return abs(arr[i]-arr[j]) + abs(i-j) 
  
def mDiff(arr,n): 
    r=0
    for i in range(0,n): 
        for j in range(i,n): 
            if (cDiff(i,j,arr)>r): 
                r=cDiff(i,j,arr) 
    return r 
  
arr=[47,23,34,-56,13,52,65,6,7,3] 
n=len(arr)
print(arr)
print(mDiff(arr,n)) 
  

