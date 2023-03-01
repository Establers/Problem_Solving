import sys
input = sys.stdin.readline

# 다익쓰트라~~
import heapq

n = int(input())
m = int(input())

graph = [ [] for _ in range(n+1) ]
distance = [int(1e9)] * (n+1)

for _ in range(m) :
    a, b, cost = map(int, input().split())
    graph[a].append( (b, cost))

start, end = map(int, input().split())

def djikstra(start) :
    q = []
    heapq.heappush(q, (0, start))  # cost 0
    distance[start] = 0

    while q :
        cost, now = heapq.heappop(q)

        if distance[now] < cost :
            continue

        for i in graph[now] :
            other_dist = cost + i[1]

            if other_dist < distance[i[0]] :
                distance[i[0]] = other_dist
                heapq.heappush(q, (other_dist, i[0]) )

djikstra(start)
print(distance[end])