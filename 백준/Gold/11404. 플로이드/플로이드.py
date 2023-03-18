import sys
ip = sys.stdin.readline

n = int(ip())
m = int(ip())

INF = int(1e9)
graph = [
    [INF] * (n+1)
    for _ in range(n+1)
]
# INF 배열로 꽉찬 2차원 배열 생성

for i in range(n+1) :
    graph[i][i] = 0
# 대각선 부분은 자기 자신으로 부터 자기 자신으로 가는 것이기 때문에 0으로 설정

for _ in range(m) :
    f, t, cost = map(int, ip().split())
    graph[f][t] = min(graph[f][t], cost)
    # 시작점과 끝점까지의 cost를 입력 받음
    # 시작점과 끝점까지의 간선이 하나가 아닐 수 있기 때문에
    # 무작정 cost를 대입하지 않고(graph[f][t] = cost) 기존 값과 비교하여 최소값만 넣음

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) : # a에서 b로 갈 때 거치는 경유점을 설정
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            # 경유점과 그냥 바로 갈 때 차이를 계산해서 최소값을 넣음
            # 이렇게 된다면 여러 점들을 타서 가는 경우도 포함해서 계산이 됨
            # 경유지를 바꿔가면서 모든 nxn을 탐색하므로

for i in range(1,n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF : graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()