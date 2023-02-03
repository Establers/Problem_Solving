import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
start = int(input())

graph = [ [] for _ in range(v+1) ]
for i in range(1,e+1) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # b : 도착지, c : 가중치(1~10)

INF = 1e9
distance = [INF for _ in range(v+1)]

def dji(start) :
    q = []
    # heapq.heappush(q, (start, 0))
    heapq.heappush(q, (0, start)) # 첫번째 값 기준으로 최소값 팝이라 반대로.
    distance[start] = 0 # 시작지점은 0

    while q :
        # 1. 큐에서 도착노드,
        dist, now = heapq.heappop(q)

        # 2. 거리 값이 더 적은지 확인
        if dist > distance[now] :
            continue

        # 3. 그래프[now]의 모든 정보에 대해
        for node in graph[now] :
            # 현재 노드의 가중치와 다음 노드 가중치 합
            distance_temp = dist + node[1] # node[1] 이 거리임

            # 지금 방문한 노드의 거리값 :distance[node[0]] 보다 작다면
            if distance_temp < distance[node[0]] :
                # 값을 갱신 후
                distance[node[0]] = distance_temp
                # q에 now 노드 추가
                # heapq.heappush(q, (node[1], distance[node[1]]))
                heapq.heappush(q, (distance[node[0]], node[0]))
                # 다음 노드에 대해 진행

dji(start)

for i in distance[1:] :
    if i == INF :
        print("INF")
    else :
        print(i)
