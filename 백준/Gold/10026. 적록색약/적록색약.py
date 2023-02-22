import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = []
visited = [ [False for _ in range(n)] for _ in range(n)]

for _ in range(n) :
    board.append(list(input().rstrip()))

def dfs(x,y) :
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx < n and 0<= ny < n) :
            if not visited[nx][ny] :
                if board[x][y] == board[nx][ny] :
                    dfs(nx, ny)

answer = [0, 0]

for i in range(n) :
    for j in range(n) :
        if not visited[i][j] :
            dfs(i, j)
            answer[0] += 1

visited = [ [False for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if board[i][j] == 'G' :
            board[i][j] = 'R'


for i in range(n) :
    for j in range(n) :
        if not visited[i][j]:
            dfs(i, j)
            answer[1] += 1

print(*answer)