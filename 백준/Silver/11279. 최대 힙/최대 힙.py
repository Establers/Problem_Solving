# 최대힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for x in range(n) :
    i = int(input())
    if i == 0 :
        if(q) :
            print(-heapq.heappop(q))
        else :
            print(0)

    else :
        heapq.heappush(q,-i)
