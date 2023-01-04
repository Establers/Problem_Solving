import sys

board = []
for i in range(5) :
    num_list = list(map(int, input().split()))
    board.append(num_list)

def find_index(num) :
    global board
    for i in range(5) :
        for j in range(5) :
            if board[i][j] == num :
                return (i, j)

# 값 받기
numbers = []
count = 0
bingo = 0
flag_ = 0
white_board = [ [0]*5 for _ in range(5) ]

for i in range(5) :
    numbers = list(map(int, input().split()))
    # print(numbers)
    for j in range(5) :
        if flag_ == 1 : break
        x, y = find_index(numbers[j])
        count += 1
        white_board[x][y] += 1 # 빈공간에 기록
        # print(white_board[2])
        bingo = 0
        for a in range(5) :
            value = 0
            # print(white_board[a])
            # print(type(white_board[a][1]))
            if white_board[a].count(1) == 5 :
            # if sum(white_board[a] == 5) :
                bingo += 1
            for b in range(5) :
                value += white_board[b][a]
                if value == 5 :
                    bingo += 1
        # print(white_board)
        value = 0
        # 대각선
        for i in range(5) :
            value += white_board[i][i]
            if value == 5 : bingo += 1

        value = 0
        for i in range(5) :
            value += white_board[i][4-i]
            if value == 5 : bingo += 1

        if bingo >= 3 :
            print(count)
            flag_ = 1
            break