n, m = map(int, input().split())
# 하나의 리스트로 관리하기 ?

# 리스트에서 달팽이로 넣는 함수
# 달팽이에서 리스트로 빼는 함수  # 빈것은 추가안하고.. 그런 식


board = []
for _ in range(n) :
    board.append(list(map(int, input().split())))

attack_list = []
for _ in range(m) :
    ad, ap = map(int, input().split())
    attack_list.append( (ad-1, ap))

atk_dir = 0
# 위 아 왼 오
atk_dx = [-1,1,0,0]
atk_dy = [0,0,-1,1]
my_x = n//2
my_y = n//2
# 아 오 위 왼 달팽이 안쪽에서 부터 채우는 것
# 왼 아 오 위
dxs = [0,  1, 0, -1]
dys = [-1, 0, 1, 0]
board_list = [0 for _ in range(n*n + 2)]
answer = 0
def in_range(x, y) :
    return 0 <= x < n and 0 <= y < n

def get_answer(val) :
    global answer
    if val == 1 :
        answer += 1
    elif val == 2 :
        answer += 2
    elif val == 3 :
        answer += 3

# 상하좌우 공격해서 가운데 좌표에서 특정 칸수만큼 0으로 바꾸는 것, in_range
def attack(a_dir, a_power) :
    global answer
    global my_x
    global my_y
    global board

    for i in range(1, a_power+1) :
        nx = my_x + (atk_dx[a_dir]) * i
        ny = my_y + (atk_dy[a_dir]) * i

        if not in_range(nx, ny) : continue
        # answer += board[nx][ny]  # 답
        # get_answer(board[nx][ny])
        board[nx][ny] = 0


# 달팽이에서 리스트로 빼는 함수  # 빈것은 추가안하고.. 그런 식
def dalpang_to_list() :
    global board
    global board_list
    temp = [0 for _ in range(n*n + 2)]

    s_x = my_x
    s_y = my_y
    move_dir = 0
    move_cnt = 1
    idx = 0
    while in_range(s_x, s_y) :
        for _ in range(move_cnt) :
            if board[s_x][s_y] != 0 :
                # 0은 추가안하고 지나감
                temp[idx] = board[s_x][s_y]
                idx += 1

            nx = s_x + dxs[move_dir]
            ny = s_y + dys[move_dir]

            s_x, s_y = nx, ny

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2 :
            move_cnt += 1

    for i in range(n*n + 2) :
        board_list[i] = temp[i]

# 리스트에서 달팽이로 넣는 함수
def list_to_dalpang() :
    global board
    global board_list
    # temp = [0 for _ in range(n*n + 2)]

    next_board = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    s_x = my_x
    s_y = my_y
    move_dir = 0
    move_cnt = 1
    idx = 0
    while in_range(s_x, s_y) :
        for _ in range(move_cnt) :
            if s_x == my_x and s_y == my_y :
                next_board[s_x][s_y] = 0
            else :
                next_board[s_x][s_y] = board_list[idx]
                idx += 1

            nx = s_x + dxs[move_dir]
            ny = s_y + dys[move_dir]

            s_x, s_y = nx, ny

        move_dir = (move_dir + 1) % 4
        if move_dir == 0 or move_dir == 2 :
            move_cnt += 1

    for i in range(n) :
        for j in range(n) :
            board[i][j] = next_board[i][j]

def four_cut() :
    global board_list
    global flag
    global answer
    flag = False

    for i in range(n*n +2) :
        if board_list[i] == 0 : continue
        now = board_list[i]
        idx_num = 1
        for j in range(i+1, n*n +2) :
            if board_list[j] == now :
                idx_num += 1
            else :
                break

        if idx_num >= 4 :
            flag = True
            for k in range(idx_num) :
                get_answer(board_list[i+k])
                board_list[i+k] = 0


    return flag

def nospace() :
    global board_list
    temp = [0 for _ in range(n * n + 2)]
    tidx = 0
    for i in range(n*n+2) :
        if board_list[i] != 0 :
            temp[tidx] = board_list[i]
            tidx += 1

    for i in range(n*n+2) :
        board_list[i] = temp[i]


def zzap() :
    global board_list

    temp = []

    for i in range(n*n +2) :
        if board_list[i] == 0 : continue
        now = board_list[i]
        board_list[i] = 0
        cnt = 1
        for j in range(i+1, n*n +2) :
            if board_list[j] == now :
                board_list[j] = 0
                cnt += 1
            else :
                break

        temp.append(cnt)
        temp.append(now)

    next_board_list = [ 0 for _ in range(n*n +2) ]

    for i in range(len(temp)) :
        if i >= n*n +2 : break
        next_board_list[i] = temp[i]

    for i in range(n*n + 2) :
        board_list[i] = next_board_list[i]


for at in attack_list :
    attack(at[0], at[1])
    dalpang_to_list()
    while True :
        f = four_cut()
        # print("fc")
        if f == False :
            break
        else :
            nospace()

    zzap()
    list_to_dalpang()
    # print(*board,sep='\n')
print(answer)