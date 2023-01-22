import math
import sys
input = sys.stdin.readline
arr = [True for _ in range(1000001)]
arr[1] = False 

m, n = map(int , input().split())

for i in range(2, int(math.sqrt(n))+1) :
    if(arr[i] == True) :
        for j in range(2*i, n+1, i) :
            arr[j] = False
            
for i in range(m,n+1) :
    if arr[i] == True :
        print(i)