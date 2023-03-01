import copy
from collections import deque

t = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 1. 터트릴 것의 좌표를 가져오는 함수
def find_removable_block(board) :
    remove_list = []

    for i in range(W) :
        for j in range(H) :
            if board[j][i] != 0 :
                remove_list.append((j, i))
                break

    return remove_list

# 2. 해당 좌표를 터뜨리기
def bomb_xy(x, y, board) :
    bomb_level = board[x][y]
    board[x][y] = 0

    for num in range(0, bomb_level) :
        for i in range(4) :
            nx = x + (dx[i] * num)
            ny = y + (dy[i] * num)

            if 0 > nx or 0 > ny or ny >= W or nx >= H : continue
            if board[x][y] == 0 : continue
            bomb_xy(nx, ny, board)
    # print(*board, sep='\n')
    return board

def bomb_xy_v2(x, y, bo) :
    board = copy.deepcopy(bo)

    q = deque()
    q.append((x, y))

    while q :
        a, b = q.popleft()
        bomb_level = bo[a][b]

        for num in range(0, bomb_level) :
            for i in range(4) :
                nx = a + (dx[i] * num)
                ny = b + (dy[i] * num)

                if 0 > nx or 0 > ny or ny >= W or nx >= H : continue
                if board[nx][ny] == 0 : continue
                board[nx][ny] = 0 # 레벨이 반영되지 않는다. 레벨은 bo에서 가져오면 되지 않을까?
                # print("펑 : ", nx, ny)
                q.append((nx, ny))

    # print("##")
    # print(*board, sep='\n')
    # print("##")
    return board


# 3. Board를 내리고 리턴하는 함수
def moving_down(board) :
    bo = copy.deepcopy(board)

    temp_board = [[ 0 for _ in range(W) ] for _ in range(H)]

    for i in range(W) :
        temp_list = []
        for j in range(H) :
            if bo[j][i] != 0 :
                temp_list.append(bo[j][i])

        for k in range(len(temp_list)-1, -1 ,-1) :
            temp_board[k + H - len(temp_list)][i] = temp_list[k]

    return temp_board

def find_all_zero(bo) :
    count = 0
    for i in range(H) :
        for j in range(W) :
            if bo[i][j] != 0 :
                count += 1
    # print(count)
    if count == 0 :
        return True
    else : return False

def bomb_back_tracking(depth, bo, re_x, re_y) :
    global answer

    if depth == N :
        count = 0
        for i in range(H) :
            for j in range(W) :
                if bo[i][j] != 0 :
                    count += 1
        # print(count)
        answer = min(answer, count)
        return

    copy_board = copy.deepcopy(bo)
    copy_board = bomb_xy_v2(re_x, re_y, copy_board)

    # 터뜨리고 나서 모두가 0 일 때 끝나야한다.
    if find_all_zero(copy_board) :
        answer = 0
        return

    copy_board = moving_down(copy_board)

    remove_list = find_removable_block(copy_board)

    for remove_posi in remove_list :
        bomb_back_tracking(depth + 1, copy_board, remove_posi[0], remove_posi[1])



for tc in range(1, t+1) :
    answer = int(1e9)
    N, W, H = map(int, input().split())

    board = []
    for _ in range(H) :
        board.append(list(map(int, input().split())))

    # MAIN LOGIC #
    remove_list = find_removable_block(board)

    # print(remove_list)

    for re_po in remove_list :
        bomb_back_tracking(0, board, re_po[0], re_po[1])

    if answer != int(1e9) :
        print("#{} {}".format(tc, answer))
    else :
        print("#{} {}".format(tc, 0))
        # 전부 0 인것 예외처리



"""
1
1 2 2
0 1
1 0
answer = 1

1
1 2 2
2 2
2 2
answer = 0

1
1 2 2
2 1
0 0
answer = 0
내 답  :1  

1
1 2 2
0 1
0 0

1
3 2 2
1 1
1 1
"""
