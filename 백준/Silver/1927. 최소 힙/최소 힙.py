import sys
import heapq
input = sys.stdin.readline

q = []

n = int(input())

for i in range(n) :
    num = int(input())
    if num == 0 :
        if(q) :
            print(heapq.heappop(q))
        else :
            print(0)
    else :
        heapq.heappush(q, num)


