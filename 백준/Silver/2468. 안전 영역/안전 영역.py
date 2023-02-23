import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
# water = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = []
visited = [[False] * n for _ in range(n)]
max_height = 0

for i in range(n) :
    li = list(map(int, input().split()))
    max_height = max(max_height, max(li))
    board.append(li)

def bfs(a, b, water):
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if(0 <= nx < n and 0 <= ny < n) :
                if board[nx][ny] > water and not visited[nx][ny] :
                    visited[nx][ny] = True
                    q.append((nx, ny))

answer = 0

for water in range(0, max_height) :
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] and board[i][j] > water :
                bfs(i, j, water)
                temp += 1

    answer = max(answer,temp)

print(answer)