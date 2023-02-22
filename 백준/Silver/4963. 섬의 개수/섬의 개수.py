import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
# 8방 탐색

def bfs(x, y) :
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q :
        x, y = q.popleft()

        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<= nx < h and 0<= ny < w and not visited[nx][ny]) :
                if board[nx][ny] == board[x][y] :
                    visited[nx][ny] = True
                    q.append((nx,ny))

while(True) : # 테케 종료
    w, h = map(int, input().split())
    if (w+h == 0) : break

    board = []
    visited = [ [False] * w for _ in range(h)]
    answer = 0
    for _ in range(h) :
        board.append(list(map(int, input().split())))

    for i in range(h) :
        for j in range(w) :
            if not visited[i][j] and board[i][j] == 1:
                bfs(i, j)
                answer += 1

    print(answer)
