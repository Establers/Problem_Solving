import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int , input().split())
board = []
for _ in range(n) :
    board.append(list(input().rstrip()))

keys = 0
K = {'a','b','c','d','e','f'}
L = {'A','B','C','D','E','F'}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

"""
1. 시작점의 위치를 찾는다 for, for
1.1 더불어 끝점의 위치도 찾는다. (필요시)

2. BFS를 통해 1을 찾기 전까지 최단거리를 찾는다.
2.0 q에는 (x, y, 이동거리, 키set) 을 넣어 계속적으로 해준다.
2.1 # 인 경우에는 가지 못한다.
2.2 abcdef 인 경우 upper를 하고 set에 넣는다(add)
2.2.1 visited 에 true를 하고 방문처리를 한다.
2.3 ABCDEF 를 만날 경우 set에 있는지 체크한다 (in)
2.4 있다면 이동하고 없다면 이동하지 않는다.
2.5 중간에 가다가 `1`을 만나면 종료 
"""

# visited = [
#     [False for _ in range(m)]
#     for _ in range(n)
# ]

visited = [
    [-1] * m # 키가 아무것도 없을 때의 방문 처리를 위해 -1로 함
    # -1 -> 0 로 키가 아무것도 없을 때 방문 처리
    for _ in range(n)
]
# 열쇠에 따른 방문처리를 진행한다.
# print(board)
q = deque()
# 1
for i in range(n) :
    for j in range(m) :
        if board[i][j] == '0' :
            visited[i][j] = 0
            board[i][j] = '.'
            q.append(
                (i, j, 0, 0)
            )
            break

def solution() :
# 2
    while q :
        x, y, dist, now_keys = q.popleft()
        # print( (x, y, dist, now_keys))
        # print(*visited, sep='\n')
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
            if board[nx][ny] == '#' : continue

            # 방문 여부 체크
            if visited[nx][ny] > -1:
                # if visited[nx][ny] == now_keys : continue
                if visited[nx][ny] | now_keys == visited[nx][ny] : continue
                # 똑같은 키로 방문한 적이 있다면 Pass

            visited[nx][ny] = now_keys

            if visited[nx][ny] == -1:
                visited[nx][ny] = 0

            if board[nx][ny] == '1' :
                return dist+1

            if board[nx][ny] == '.' :
                # visited[nx][ny] = True
                q.append(
                    (nx, ny, dist+1, now_keys)
                )
                continue

            if board[nx][ny] in K : # a-f
                temp = ord(board[nx][ny]) - 97 # 0~5
                # now_keys |= (1<<temp) # bit on
                new_keys = now_keys | (1<<temp)
                # print("nowkeys :", now_keys, 1<<temp)
                # visited[nx][ny] = now_keys
                q.append(
                    (nx, ny, dist+1, new_keys)
                )
                continue

            if board[nx][ny] in L : # A-F
                temp = ord(board[nx][ny]) - 65 # 0~5
                # 열쇠 가지고 있는지 체크
                # print(now_keys, (1<<temp))
                # visited[nx][ny] = now_keys
                if now_keys & (1<<temp) != 0 :
                    # 가지고 있음
                    q.append(
                        (nx, ny, dist+1, now_keys)
                    )
                    continue

    return -1

print(solution())