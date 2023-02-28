import sys
input = sys.stdin.readline
from collections import deque
# 벽에 진입 -> 게임 끝
# 자기 몸에 진입 -> 게임 끝 몸인곳 1?
dx = [0,1, 0,-1]
dy = [1,0,-1,0 ]
# 오른쪽, 아래, 왼쪽, 위 순

n = int(input()) # 보드 크기 N N
board = [[ 0 for _ in range(n)] for _ in range(n)]
apple_board = [[ 0 for _ in range(n)] for _ in range(n)]

k = int(input()) # 사과 개수
for _ in range(k) :
    x, y = map(int, input().split())
    x += -1
    y += -1 # indexing 처리
    apple_board[x][y] = 1 # 사과는 10이야!


l = int(input()) # 명령어 개수
com_list = deque()
for _ in range(l) :
    com_list.append(list(input().rstrip().split()))

count = 0
q = deque()
q.append((0,0))
dir = 0

while(True) :
    count += 1
    now_x, now_y = q[-1]
    # print(now_x, now_y)

    next_x = now_x + dx[dir]
    next_y = now_y + dy[dir]

    if com_list and int(com_list[0][0]) == count :
        if com_list[0][1] == 'D' :
            dir += 1
            if dir == 4 :
                dir = 0
        else : # L
            dir += -1
            if dir == -1 :
                dir = 3

        com_list.popleft()

    # next_x = now_x + dx[dir]
    # next_y = now_y + dy[dir]

    if (next_x < 0 or next_x >= n or next_y < 0 or next_y >= n) : break # 벽에 부딪힘
    if (next_x, next_y) in q : break # 몸에 부딪힘
    # 정상 경우 일 때
    q.append((next_x, next_y))

    if apple_board[next_x][next_y] == 0 :
        q.popleft()
    else :
        apple_board[next_x][next_y] = 0


print(count)