import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

# 나이트 오른쪽 위 부터 시계방향으로 계산
dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]

def in_range(x, y) :
    return 0 <= x < l and 0 <= y < l

for _ in range(t) :

    answer = float('inf')
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited = [
        [False for _ in range(l)]
        for _ in range(l)
    ]

    q = deque()
    q.append((sx, sy, 0)) # 초기 위치
    visited[sx][sy] = True

    while q :
        x, y, m = q.popleft()

        # 끝나는 조건 확인
        if (x, y) == (ex, ey) :
            answer = min(answer, m)

        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]

            if not in_range(nx, ny) : continue
            if not visited[nx][ny] :
                q.append((nx, ny, m+1))
                visited[nx][ny] = True

    print(answer)