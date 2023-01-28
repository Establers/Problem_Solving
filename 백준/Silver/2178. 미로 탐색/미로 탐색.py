import sys
sys = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())

graph = []

for i in range(n) :
    lines = list(map(int, input()))
    graph.append(lines)


# 1 이동 가능, 0 이동 불가
# 1,1 (맨왼쪽위에서 출발) 0,0 으로 할 예정
# 맨 오른쪽 아래가 도착 지점

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y) :
    q = deque()
    q.append((x,y))

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동할 곳이 외부인 경우,
            if (0 <= nx < n and 0 <= ny < m) != True :
                continue
            else :
                # 못가는 땅
                if (graph[nx][ny] == 0):
                    continue
                elif (graph[nx][ny] == 1): #처음 방문 하는 땅
                    graph[nx][ny] = graph[x][y] + 1
                    # 이 때 까지 이동한 거리 누적
                    q.append((nx, ny))
                    # 새로운 곳 이동

    return graph[n-1][m-1]

print(bfs(0,0))
