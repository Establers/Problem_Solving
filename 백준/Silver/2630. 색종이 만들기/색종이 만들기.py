import sys
input = sys.stdin.readline

n = int(input())

answer_blue = 0
answer_white = 0

board = []
for i in range(n)  :
    board.append(list(map(int, input().split())))

def checkAll(n, x_idx, y_idx) :
    global answer_blue
    global answer_white
    count_blue = 0
    for i in range(x_idx, n + x_idx) :
        for j in range(y_idx, n + y_idx) :
            count_blue += board[i][j]

    if count_blue == n**2 :
        answer_blue += 1
        return True

    elif count_blue == 0 : # white
        answer_white += 1
        return True

def bt(n, x, y)  :
    global answer_blue
    global answer_white

    if(checkAll(n, x, y)) : return True

    bt(n//2, x, y)
    bt(n//2, x+n//2, y)
    bt(n//2, x, y + n//2)
    bt(n//2, x+n//2, y+n//2)


bt(n, 0, 0)
print(answer_white)
print(answer_blue)