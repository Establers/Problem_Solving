import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int ,input().split())
graph = []

for i in range(n) :
    list_ = list(map(int, input().split()))
    graph.append(list_)
    #graph[0~3][0~5] # 예제1
    #graph[n][m]
q = deque()

dx = [1,-1, 0, 0]
dy = [0, 0, 1,-1]

def bfs() :
    # 1. 1 찾아서 큐에 넣기
    for i in range(m) :
        for j in range(n) :
            if graph[j][i] == 1 :
                q.append( (j,i) )

    # 1-2. 큐가 빌때까지 위 과정 진행
    while q :
        #print(q)
        y, x = q.popleft()

        #print(y,x)
        count = 0
        for i in range(4) : # dx dy
            nx = x + dx[i] # m
            ny = y + dy[i] # n
            if (0 <= nx < m and 0 <= ny < n) == False :
                continue # 맵 밖.

            # 2. 1 상하좌우 0-> 1로 만들고 다시 큐에 넣기 (범위 안넘치게)
            else :
                count += 1
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((ny, nx))

                # 3. 단 -1 일 경우, 변경X
                elif graph[ny][nx] == -1:
                    continue

# 4. 큐가 비었고, 만약 맵에 0이 있다면, -1
def solution() :
    count_day = 0
    bfs()
    for i in graph :
        for j in i :
            if j == 0:
                print(-1)
                return

        count_day = max(count_day, max(i))
    print(count_day - 1)

solution()