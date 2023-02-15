import sys
input = sys.stdin.readline
import heapq

n = int(input())

min_q = []
max_q = []
mid_value = 0

for i in range(1,n+1) :
    num = int(input())

    if (i == 1) :
        mid_value = num
        heapq.heappush(min_q, -(num))
        print(num)
    else :  # peek 활용
        if(not max_q) :
            if (num > -min_q[0]) :
                # max_q에 들어가야함
                heapq.heappush(max_q, num)
                print(-min_q[0])
            else :
                heapq.heappush(min_q, -num)
                if (len(min_q) >= len(max_q) + 2):
                    heapq.heappush(max_q, -heapq.heappop(min_q))
                print(-min_q[0])
        elif (-min_q[0] <= num <= max_q[0]) : # 새로운 중간값
            mid_value = num
            heapq.heappush(min_q, -(num))
            if (len(min_q) >= len(max_q) + 2):
                heapq.heappush(max_q, -heapq.heappop(min_q))
            print(-min_q[0])
        elif (num > max_q[0]) :
            # max_q의 최소값 s보다 크다 -> max_q에 넣기
            # 길이 비교
            if (len(min_q) <= len(max_q)) :
                heapq.heappush(min_q, -heapq.heappop(max_q))

            heapq.heappush(max_q, num)
            print(-min_q[0])
        elif (num < -min_q[0]) :
            heapq.heappush(min_q, -(num))
            if (len(min_q) >= len(max_q)+2) :
                heapq.heappush(max_q, -heapq.heappop(min_q))
            print(-min_q[0])

    # print(min_q, "\n", max_q,sep='')