import sys
input = sys.stdin.readline
import heapq

tc = int(input())

for _ in range(tc) :
    n = int(input())
    seq = list(map(int, input().split()))
    hq = []
    answer = 1
    if n == 1 :
        answer = 1
        print(answer)
        continue

    for a in seq :
        heapq.heappush(hq, a)

    for _ in range(n-1) :
        a = heapq.heappop(hq)
        b = heapq.heappop(hq)
        c = (a * b) 
        answer = (answer * c) 

        heapq.heappush(hq, c)

    print(answer % 1000000007)

"""
3
2
1999999999 1999999999
1
13
2
2 2
"""