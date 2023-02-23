import sys
input = sys.stdin.readline
from collections import deque
# import itertools
# 삼성 itertools 안댐

import copy

n, m, Distance = map(int, input().split())
# 행, 열, 공격거리 제한
answer = 0
board = []

dx = [0, -1, 0]
dy = [-1, 0, 1]

for i in range(n) :
    board.append(list(map(int, input().split())))
    # 0 : 빈칸, 1 : 적

# archer_comb = list(itertools.combinations(range(m), 3))

# 0 1 2 3 4 .. m-1 까지의 조합을 구하면 됨
archer_comb = []
for i in range(1, 1<<m) :
    temp = []
    for j in range(m) :
        if i & (1<<j) != 0 :
            temp.append(j)
    if len(temp) == 3 :
        archer_comb.append(temp)


for ar in archer_comb :
    # 구현 지점
    result = 0
    visited = [[False] * m for _ in range(n)]
    board_copy = copy.deepcopy(board)

    # print("NEW")
    for i in range(n-1, -1, -1) :
        # day
        to_be_changed_board = []

        for archer in ar :
            q = deque()
            q.append((i,archer,1))

            while q :
                x, y, d = q.popleft() # 내가 죽일 수 있는 값의 좌표
                # 죽일 수 있는지 체크

                if board_copy[x][y] == 1:
                    to_be_changed_board.append((x, y))
                    if not visited[x][y] : # 죽였음을 체크
                        visited[x][y] = True
                        # print(x, y)
                        result += 1
                    break # 죽임

                # 거리가 지금 더 작으면 한번 더 늘려준다
                if d < Distance :
                    for idx in range(3) :
                        nx = x + dx[idx]
                        ny = y + dy[idx]
                        if (0 <= nx < n and 0 <= ny < m) :
                            q.append((nx, ny, d+1))

        for a, b in to_be_changed_board :
            board_copy[a][b] = 0

    answer = max(answer, result)



print(answer)