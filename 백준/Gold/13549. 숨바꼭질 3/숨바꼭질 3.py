import sys
input = sys.stdin.readline
import heapq

n, k = map(int, input().split())
INF = int(1e9)

distance = [INF] * (100000+1)

def djikstra(start) :
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q :
        now_time, now = heapq.heappop(q)

        if distance[now] < now_time :
            continue

        # 3가지 CASE
        new_time = now_time + 1

        if now + 1 <= 100000 :
            if new_time < distance[now + 1] :
                distance[now + 1] = new_time
                heapq.heappush(q, (new_time, now + 1))

        if 0 <= now - 1 :
            if new_time < distance[now - 1] :
                distance[now - 1] = new_time
                heapq.heappush(q, (new_time, now - 1))

        if now * 2 <= 100000 :
            if now_time < distance[now * 2] :
                distance[now * 2] = now_time
                heapq.heappush(q, (now_time, now * 2))

djikstra(n)
print(distance[k])
# print(distance)