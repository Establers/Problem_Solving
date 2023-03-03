import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

board = []
next_board = [[ 0 for _ in range(C)] for _ in range(R)]

for _ in range(R):
    board.append(list(map(int, input().split())))

# 공기 청정기 위쪽 꺼, 아래쪽 꺼 찾기
air_cleaner = []
for i in range(R) :
    for j in range(C) :
        if board[i][j] == -1 :
            air_cleaner.append( (i, j) )

air_cleaner_up = air_cleaner[0]
air_cleaner_down = air_cleaner[1]

# 1. 확산을 next_board에 적용한다.
# 값이 -1에는 적용안하고, count에 포함하지 않음
def diffusion() :
    global board
    next_board = [[0 for _ in range(C)] for _ in range(R)]

    count = 0
    for x in range(R):
        for y in range(C) :
            count = 0
            if board[x][y] != -1 and board[x][y] != 0 :
                # 확산할 수 있는 경우
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < R and 0 <= ny < C : # 경계안
                        if board[nx][ny] == -1: continue  # 공기청정기 pass
                        next_board[nx][ny] += (board[x][y] // 5)
                        count += 1

                # 확산이 끝났으니 count 만큼 본인 것 감소
                next_board[x][y] += (board[x][y] - (board[x][y] // 5) * count)

    # 확산 완전 종료
    # 원래 보드에 복사
    for i in range(R) :
        for j in range(C) :
            board[i][j] = next_board[i][j]

    board[air_cleaner_up[0]][air_cleaner_up[1]] = -1
    board[air_cleaner_down[0]][air_cleaner_down[1]] = -1

def swap(a,b, c,d) :
    global board
    temp = board[a][b]
    board[a][b] = board[c][d]
    board[c][d] = temp


def up_rotaion() :
    global board
    half_x = air_cleaner_up[0] + 1

    for a in range(0, C-1) :
        swap(0, a, 0, a+1)

    for a in range(0, half_x - 1) :
        swap(a, C-1, a+1, C-1)

    for a in range(C-1, 0, -1) :
        swap(half_x - 1, a, half_x - 1, a-1)

    for a in range(half_x - 1, 1, -1) :
        swap(a,0, a-1,0)

    for i in range(half_x) :
        for j in range(C) :
            if board[i][j] == -1 :
                board[i][j] = 0

    board[air_cleaner_up[0]][air_cleaner_up[1]] = -1


def down_rotation() :
    global board
    half_x = air_cleaner_down[0]
    # x = 3,4,5,6 -> R-1까지 돔
    # half_x = acd[0] = 3
    # print(half_x)
    for a in range(0, C-1) :
        swap(R-1, a, R-1, a+1)

    for a in range(R-1, half_x, -1) :
        swap(a, C-1, a-1, C-1)

    for a in range(C-1, 0, -1) :
        swap(half_x, a, half_x, a-1)

    for a in range(half_x, R-2) :
        swap(a,0, a+1, 0)


    for i in range(half_x, R) :
        for j in range(C) :
            if board[i][j] == -1 :
                board[i][j] = 0

    board[air_cleaner_down[0]][air_cleaner_down[1]] = -1


# MAIN LOGIC

for _ in range(T) :
    # print(*board, sep='\n')
    # print("######")
    diffusion()

    # print(*board, sep='\n')
    # print("###### 위에 회전")
    up_rotaion()
    # print(*board, sep='\n')

    # print("###### 밑에 회전 ")
    down_rotation()
    # print(*board, sep='\n')
    # print("######")

answer = 0
for i in range(R) :
    for j in range(C) :
        if board[i][j] == -1 : continue
        if board[i][j] > 0 :
            answer += board[i][j]

# print(*board,sep='\n')
print(answer)