import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

for a in range(n) :
    str = input().rstrip()
    graph.append(list(map(int, str)))


dx = [1, -1, 0,  0]
dy = [0,  0, 1, -1]

# visited = [[False for _ in range(m)] for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

visited[0][0][0] = 1

def bfs() :
    global result
    q = deque()
    q.append((0,0,0)) # x, y, 0 : 벽 부술 수 있음, 1 부쉈음

    while q:
        x, y, wall = q.popleft()

        if (x == n - 1 and y == m - 1):
            print(visited[x][y][wall])
            return

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if(nx < 0 or ny < 0 or nx >= n or ny >= m) :
                continue
            else :
                if(graph[nx][ny] == 1 and wall == 0) :
                    # 부수고 이동
                    visited[nx][ny][1] = visited[x][y][wall] + 1
                    q.append((nx, ny, 1))
                elif(graph[nx][ny] == 0 and visited[nx][ny][wall] == 0) :
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx,ny,wall))

            # if(nx == n-1 and ny == m-1) :
            #     print(visited[nx][ny][wall])
            #     return
    # 큐가 빌때까지 못왔으면
    print(-1)
    return

bfs()

