# 최단경로 정점 1로 가는 + 간선COST + v2에서 n까지 가는 최단경로

import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
# distance = [ int(1e9) ] * (n+1)
graph = [ [] for _ in range(n+1)]

for _ in range(m) :
    a, b, cost = map(int, input().split())
    graph[a].append( (cost, b) )
    graph[b].append( (cost, a) )

def djikstra(start)  :
    q = []
    distance[start] = 0 # 출발점은 0
    heapq.heappush(q, (0, start))

    while q :
        cost, now = heapq.heappop(q)

        if distance[now] < cost :
            continue

        for i in graph[now] :
            other_cost = cost + i[0]

            if other_cost < distance[i[1]] :
                distance[i[1]] = other_cost
                heapq.heappush(q, (other_cost, i[1]))


v1, v2 = map(int, input().split())


# 1번에서 출발을 한다

answer_v1_to_v2 = 0
answer_v2_to_v1 = 0

distance = [int(1e9)] * (n + 1)
djikstra(1)
# print(distance)
# answer += distance[v1]
answer_v1_to_v2 += distance[v1]
answer_v2_to_v1 += distance[v2]

distance = [ int(1e9) ] * (n+1)
djikstra(v2)
# print(distance)
# answer += distance[n]
answer_v1_to_v2 += distance[n]

distance = [ int(1e9) ] * (n+1)

djikstra(v1)
# print(distance)
answer_v2_to_v1 += distance[n]

# 이건 짧은 거리가 아니다... 바로 연결되어있다고 짧은게 아님!
# edge = int(1e9)
# for i in graph[v1] :
#     if i[1] == v2  :
#         edge = i[0]
####

distance = [ int(1e9) ] * (n+1)
djikstra(v1)
edge = distance[v2]

answer_v1_to_v2 += edge
answer_v2_to_v1 += edge

answer = min(answer_v1_to_v2, answer_v2_to_v1)

if answer >= int(1e9) :
    print(-1)
else :
    print(answer)