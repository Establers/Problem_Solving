import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단 거리 형식으로 식나을 구해야한다.
n = int(input())
board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

my_size = 2
# input end

# 최단 거리를 구하기 위한 dist_board
# dist_board = [[ -1 for _ in range(n) ] for _ in range(n)]

# 9의 위치를 찾기
def find_shark() :
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9 :
                x, y = i, j
                break
    return x, y

def find_eatable_fish(dist_board) :
    # 자신 보다 작은 사이즈의 물고기만 먹을 수 있다.
    global my_size
    global board

    x, y = -1, -1
    shortest_dist = int(1e9)

    for i in range(n) :
        for j in range(n) :
            if board[i][j] >= my_size : continue
            if board[i][j] == 0 : continue
            if dist_board[i][j] == -1 : continue
            if dist_board[i][j] < shortest_dist :
                # print(board[i][j], my_size)
                x, y = i, j
                shortest_dist = dist_board[i][j]

    return x, y, shortest_dist

def bfs(x, y) :
    q = deque()
    q.append( (x, y) )

    # 최단 거리를 구하기 위한 dist_board
    dist_board = [[-1 for _ in range(n)] for _ in range(n)]
    dist_board[x][y] = 0 # visited

    while q :
        a, b = q.popleft()

        for i in range(4) :
            na = a + dx[i]
            nb = b + dy[i]

            if 0 > na or 0 > nb or na >= n or nb >= n : continue
            if my_size >= board[na][nb] :
                if dist_board[na][nb] == -1 :
                    # not visited
                    dist_board[na][nb] = dist_board[a][b] + 1
                    q.append( (na, nb) )

    return dist_board
# MAIN LOGIC #

now_x, now_y = find_shark()
board[now_x][now_y] = 0
times = 0
eat_count = 0

while True :
    # find_eatable_fish 가 -1, -1 -> end
    shortest_distance_board = bfs(now_x, now_y)
    # print(*shortest_distance_board, sep='\n')
    x, y, dist = find_eatable_fish(shortest_distance_board)
    if x == -1 and y == -1 and dist == int(1e9) : break
    # print(x, y, dist)

    times += dist
    # print("tiems ", times)
    board[x][y] = 0 # eat
    eat_count += 1
    if eat_count == my_size :
        my_size += 1
        eat_count = 0

    now_x = x
    now_y = y
    # print(*board, sep='\n')

print(times)