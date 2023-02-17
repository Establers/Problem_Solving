import sys
input = sys.stdin.readline
import heapq

seq = []

n = int(input())

for i in range(n) :
    heapq.heappush(seq, int(input()))

result = 0

while(len(seq) >= 2) :
    a = heapq.heappop(seq)
    b = heapq.heappop(seq)
    #print(a,b)
    result += a+b
    heapq.heappush(seq, a+b)

print(result)

