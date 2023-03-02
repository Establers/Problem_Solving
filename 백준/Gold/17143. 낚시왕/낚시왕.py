import sys
input = sys.stdin.readline
import copy

R, C, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

board = [ [ [] for _ in range(C)] for _ in range(R)]

for _ in range(M) :
    # 상어 r, c 속력 s, d 이동 방향, z 크기
    r,c,s,d,z = map(int, input().split())
    r = r-1
    c = c-1
    shark_temp = [r, c, s, d, z]
    board[r][c].append(shark_temp)

def moving_shark() :
    global board
    board_moved = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R) :
        for j in range(C) :
            if board[i][j] == [] : continue
            t_s = board[i][j][0]

            if t_s[3] == 3 : # 오른쪽 무빙
                # c만 변경된다.
                init_idx = t_s[1]
                speed = t_s[2]

                direction = 1

                while speed > 0:
                    speed += -1

                    init_idx += (1 * direction)

                    if init_idx == -1:
                        init_idx = 1
                        direction = 1

                    elif init_idx == C:
                        init_idx = C - 2
                        direction = -1

                    if speed == 0:
                        break

                t_s[1] = init_idx

                if direction == -1:
                    t_s[3] = 4

                board_moved[i][t_s[1]].append(t_s)


            elif t_s[3] == 4 : # 왼쪽방향
                init_idx = t_s[1]
                speed = t_s[2]

                direction = -1

                while speed > 0 :
                    speed += -1

                    init_idx += (1 * direction)

                    if init_idx == -1 :
                        init_idx = 1
                        direction = 1

                    elif init_idx == C :
                        init_idx = C - 2
                        direction = -1

                    if speed == 0 :
                        break

                t_s[1] = init_idx

                if direction == 1 :
                    t_s[3] = 3

                board_moved[i][t_s[1]].append(t_s)


            elif t_s[3] == 2 : # 아래 방향
                init_idx = t_s[0]
                speed = t_s[2]

                direction = 1

                while speed > 0:
                    speed += -1

                    init_idx += (1 * direction)

                    if init_idx == -1:
                        init_idx = 1
                        direction = 1

                    elif init_idx == R:
                        init_idx = R - 2
                        direction = -1

                    if speed == 0:
                        break

                t_s[0] = init_idx

                if direction == -1:
                    t_s[3] = 1
                # print(t_s)
                board_moved[t_s[0]][j].append(t_s)


            elif t_s[3] == 1 : # 위 방향
                init_idx = t_s[0]
                speed = t_s[2]

                direction = -1

                while speed > 0:
                    speed += -1

                    init_idx += (1 * direction)

                    if init_idx == -1:
                        init_idx = 1
                        direction = 1

                    elif init_idx == R:
                        init_idx = R - 2
                        direction = -1

                    if speed == 0:
                        break

                t_s[0] = init_idx

                if direction == 1:
                    t_s[3] = 2

                board_moved[t_s[0]][j].append(t_s)

    board = copy.deepcopy(board_moved)


def eatting_shark() :
    global board

    for i in range(R) :
        for j in range(C) :
            if board[i][j] == [] : continue
            remain_shark = []
            if len(board[i][j]) >= 2 :
                board[i][j].sort(key = lambda x : x[4], reverse = True)
                remain_shark = board[i][j][0]
                board[i][j] = []
                board[i][j].append(remain_shark)


result = 0

for i in range(C) : # 낚시꾼 Moving
    for j in range(R) :
        if board[j][i] :
            # print("KILL : ", board[j][i])
            result += board[j][i][0][4]
            board[j][i] = []
            break

    moving_shark()
    eatting_shark()


# print("########")
print(result)
# print(*board, sep='\n')