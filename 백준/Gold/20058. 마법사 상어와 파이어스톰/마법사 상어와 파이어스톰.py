import sys

input = sys.stdin.readline
from collections import deque

board = []
n, q = map(int, input().split())
max_size = int(1 << n)
for _ in range(max_size):
    board.append(list(map(int, input().split())))

levels = list(map(int, input().split()))

next_board = [
    [0 for _ in range(max_size)]
    for _ in range(max_size)
]

# 오, 아, 위, 왼 # 0 1 2 3
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]


def rot(sx, sy, half_size, move_dir):
    global board
    global next_board

    for i in range(sx, sx + half_size):
        for j in range(sy, sy + half_size):
            ii = i + dx[move_dir] * half_size
            jj = j + dy[move_dir] * half_size
            next_board[ii][jj] = board[i][j]

def rot2(sx, sy, box_size):
    global board
    global next_board
    # print(sx, sy)
    for i in range(sx, sx + box_size):
        idx = sx
        for j in range(sy, sy + box_size):
            # next_board[j][box_size - i - 1] = board[i][j]
            next_board[idx][(sx+sy+box_size) - i - 1] = board[i][j]
            # print("board", i, j)
            idx += 1


def divide(level):
    if level == 0:
        return
    global board
    global next_board

    for i in range(max_size):
        for j in range(max_size):
            next_board[i][j] = 0

    box_size = int(2 ** level)
    half_size = int(2 ** (level - 1))

    for i in range(0, max_size, box_size):
        for j in range(0, max_size, box_size):
            # print("ij", i,j)
            # rot(i, j, half_size, 0)
            # rot(i, j + half_size, half_size, 1)
            # rot(i + half_size, j, half_size, 2)
            # rot(i + half_size, j + half_size, half_size, 3)
            rot2(i, j, box_size)
            # rot2(i, j + box_size, box_size)
            # rot2(i + box_size, j, box_size)
            # rot2(i + box_size, j + box_size, box_size)


    for i in range(max_size):
        for j in range(max_size):
            board[i][j] = next_board[i][j]


def in_range(x, y):
    return 0 <= x < max_size and 0 <= y < max_size


# 얼음 녹기
def melting_ice():
    global board
    global next_board

    for i in range(max_size):
        for j in range(max_size):
            next_board[i][j] = 0

    for i in range(max_size):
        for j in range(max_size):
            count = 0
            if board[i][j] == 0: continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if in_range(nx, ny) and board[nx][ny] > 0:
                    count += 1

            if count < 3:
                # 얼음이 녹음
                next_board[i][j] = board[i][j] - 1
            else:
                next_board[i][j] = board[i][j]

    for i in range(max_size):
        for j in range(max_size):
            board[i][j] = next_board[i][j]


max_goonzip = 0
visited = [
    [False for _ in range(max_size)]
    for _ in range(max_size)
]


def bfs(a, b):
    temp_sum = 0
    q = deque()
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        temp_sum += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx, ny):
                if not visited[nx][ny] and board[nx][ny] != 0:
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return temp_sum


all_ice = 0


def all_sum():
    global all_ice
    global board

    for i in range(max_size):
        for j in range(max_size):
            all_ice += board[i][j]

#
# divide(1)
# print(*board, sep='\n')

#### SIMULATION ####
for lv in levels:
    if lv > 0 :
        divide(lv)
    melting_ice()

# print(*board,sep='\n')
for i in range(max_size):
    for j in range(max_size):
        if not visited[i][j] and board[i][j] > 0:
            mg = bfs(i, j)
            # print(mg)
            max_goonzip = max(max_goonzip, mg)

# print(*board,sep='\n')
all_sum()
print(all_ice)
print(max_goonzip)