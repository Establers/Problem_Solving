n, m = map(int, input().split())

# 오
# dx = [0,-1,-1,-1,0,1,1,1]
# dy = [1,1,0,-1,-1,-1,0,1]

dx = [0, -1, -1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

command = []
for _ in range(m) :
    movedir, movetime = map(int, input().split())
    temp = []
    temp.append(movedir-1)
    temp.append(movetime)
    command.append(temp)

yung_yang = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 초기 영양제 위치
for i in range(n-1, n-3, -1) :
    for j in range(0, 2) :
        yung_yang[i][j] = 1
        # 1 영양제 위치

# print(*yung_yang, sep='\n')

# 대각선 탐색 전용
dxs = [-1,-1,1,1]
dys = [1,-1,-1,1]

def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

# 1. 영양제 움직임 초과하는 것은 (idx + times*dx,dy[movedir]) % 5 로 다시 계산
for comm in command :
    # movedir, movetime
    next_yy = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            if yung_yang[i][j] == 1 :
                nx = (i + dx[comm[0]] * comm[1] + comm[1]*n) % n
                ny = (j + dy[comm[0]] * comm[1] + comm[1]*n) % n

                next_yy[nx][ny] = 1
    # print("아래. 전")
    # print(*yung_yang, sep='\n')
    # print("")
    # print(*next_yy, sep='\n')
    # print("")
    # print(*board,sep='\n')
    # print("위. 후")
    for i in range(n) :
        for j in range(n) :
            yung_yang[i][j] = next_yy[i][j]

    # 2. 영양제가 움직이고 나서 영양제 위치의 board에 1을 증가
    yy_set = set()
    for i in range(n) :
        for j in range(n) :
            if yung_yang[i][j] == 1:
                yy_set.add((i, j))
                board[i][j] += 1

    # 3. 영양제 인덱스의 대각선 4방향을 보고 영양제 인덱스에 해당하는 board에 +n만큼 추가
    for i in range(n):
        for j in range(n):
            cnt = 0
            if yung_yang[i][j] == 1 :
                for k in range(4) : # 대각선 전용
                    ni = i + dxs[k]
                    nj = j + dys[k]

                    if not in_range(ni, nj) : continue
                    if board[ni][nj] >= 1 :
                        cnt += 1

                board[i][j] += cnt

    # 영
    for i in range(n) :
        for j in range(n) :
            next_yy[i][j] = 0

    # 4. 모든 보드에서 2이상인 값 0으로 하고, 다시 그 위치에 영양제 보드 1 추가,
    for i in range(n) :
        for j in range(n) :
            if yung_yang[i][j] == 1 :
                yung_yang[i][j] = 0 # 영양제 소모
                continue
            if board[i][j] >= 2 :
                board[i][j] += -2
                next_yy[i][j] = 1 # 새 영양제 추가
                # 4.1 단 이번에 영양제 있던 위치를 제외하고

    for i in range(n) :
        for j in range(n) :
            yung_yang[i][j] = next_yy[i][j]

answer = 0
for i in range(n) :
    for j in range(n) :
        answer += board[i][j]

print(answer)



