import math
import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))

d = [ True for i in range(1001)] # true 소수

d[0:1] = False, False

for i in range(2, int(math.sqrt(1000))+1) :
    if d[i] == True :
        for j in range(i+i, 1001, i) :
            if d[j] == True :
                d[j] = False

count = 0
for i in numList :
    if d[i] == True :
        count += 1

print(count)



