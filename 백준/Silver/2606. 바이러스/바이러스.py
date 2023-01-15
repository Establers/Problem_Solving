import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터 수
m = int(input()) # 직접 연결되어 있는 컴퓨터 쌍의 수 # 노드 수
INF = int(1e9)
graph = [ [INF] * (n+1) for i in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    # a 노드 b 노드는 연결되어 있다.
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
for i in graph[1] :
    if i != INF :
        count += 1

print(count-1)