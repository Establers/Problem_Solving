import sys
input = sys.stdin.readline
import heapq

n, m, x = map(int, input().split())
# n명의 학생, m개의 간선, x번 마을이 모이는 곳

distance_go = [ int(1e9) ] * (n+1)
distance_back = [ int(1e9) ] * (n+1)
graph = [ [] for _ in range(n+1) ]
answer = [0] * (n+1)

# 시작, 끝, Time
for i in range(m) :
    a, b, time = map(int, input().split())
    graph[a].append( (time, b) )






def djikstra(start, distance : list)  :
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q :
        time, now = heapq.heappop(q)

        if distance[now] < time :
            continue

        # 주변 도로 확인
        for i in graph[now] :
            other_time = time + i[0]

            if other_time < distance[i[1]] :
                distance[i[1]] = other_time
                heapq.heappush(q, (other_time, i[1]))


# N번에서 X로 가는 시간
for i in range(1, n+1) :
    distance_go = [int(1e9)] * (n + 1)
    djikstra(i, distance_go)
    answer[i] += distance_go[x]

# X에서 N으로 가는 시간
distance_back = [int(1e9)] * (n + 1)
djikstra(x, distance_back)
for i in range(1, n+1) :
    answer[i] += distance_back[i]

print(max(answer))