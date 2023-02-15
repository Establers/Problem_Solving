import sys
input = sys.stdin.readline
import heapq

n = int(input())
q1 = []
q2 = []

for _ in range(n) :
    num = int(input())

    if num != 0 :
        if num > 0 :
            heapq.heappush(q1,  num)
        else :
            heapq.heappush(q2, -num)

    else :
        if (q1 or q2) :
            if(len(q1) == 0):
                print(-heapq.heappop(q2))
                continue
            elif(len(q2) == 0) :
                print(heapq.heappop(q1))
                continue
            min_value = heapq.heappop(q1)
            max_value = heapq.heappop(q2)
            if (abs(min_value) < abs(max_value)) :
                print(min_value)
                heapq.heappush(q2,max_value)
            else :
                print(-max_value)
                heapq.heappush(q1, min_value)

        else :
            print(0)

