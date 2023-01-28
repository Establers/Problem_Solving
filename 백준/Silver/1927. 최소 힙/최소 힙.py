import heapq
import sys
input = sys.stdin.readline

n = int(input())

q = []

for i in range(n) :
    a = int(input())
    if a > 0 :
        heapq.heappush(q, a)
    elif a == 0 :
        if q :
            print(heapq.heappop(q))
        else : # 큐가 비어있을 경우
            print(0)