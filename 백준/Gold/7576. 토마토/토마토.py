import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())

board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n) :
    board.append(list(map(int, input().split())))

# 짱멋진 BFS로 10분컷 해보기~ 23:55 시작

visited = [ [ False for _ in range(m)] for _ in range(n)]

q = deque()

for i in range(n) :
    for j in range(m) :
        if board[i][j] == 1:
            q.append( (i, j) )

while q :
    x, y = q.popleft()

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 > nx or 0 > ny or nx >= n or ny >= m : continue
        if board[nx][ny] == -1 : continue
        if board[nx][ny] == 0 :
            board[nx][ny] = board[x][y] + 1
            q.append( (nx , ny))

# print(*board, sep='\n')
def solution() :
    answer = 0

    for i in range(n) :
        for j in range(m) :
            answer = max(answer, board[i][j])
            if board[i][j] == 0 :
                print(-1)
                return

    print(answer - 1)

solution()