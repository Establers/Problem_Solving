import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split())

a = []
for _ in range(h) :
    a.append(list(map(int, input().split())))

INT_MAX = int(2e9)
dp = [
    [ [ INT_MAX for _ in range(k+1)] for _ in range(w)]
    for _ in range(h)
]
# [] [] []
# x  y   k(나이트 무빙 횟수)에 따른 최소 행동

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dnx = [2, 1, -1, -2, -2, -1, 1, 2]
dny = [1, 2, 2, 1, -1, -2, -2, -1]
# init
def init() :
    for i in range(k+1) :
        dp[0][0][i] = 0

init()

# 큐에 k를 세기위한 cnt도 넣는다.
# bfs
q = deque()
q.append( (0, 0, 0)) # x y cnt(나이트 무빙)

while q :
    x, y, c = q.popleft()

    # Knight
    if c < k :
        for i in range(8) :
            nx = x + dnx[i]
            ny = y + dny[i]

            if nx < 0 or ny < 0 or nx >= h or ny >= w : continue
            if a[nx][ny] == 1 : continue
            if dp[nx][ny][c+1] > dp[x][y][c] + 1 :
                dp[nx][ny][c+1] = dp[x][y][c] + 1
                q.append( (nx, ny, c + 1) )

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= h or ny >= w: continue
        if a[nx][ny] == 1: continue
        if dp[nx][ny][c] > dp[x][y][c] + 1:
            dp[nx][ny][c] = dp[x][y][c] + 1
            q.append((nx, ny, c))

# print(*dp, sep='\n')
if min(dp[h-1][w-1]) == INT_MAX :
    print(-1)
else :
    print(min(dp[h-1][w-1]))