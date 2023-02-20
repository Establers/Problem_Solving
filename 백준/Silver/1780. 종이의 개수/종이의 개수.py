import sys
input = sys.stdin.readline

n = int(input())
board = []
answer_minus1 = 0
answer_plus1 = 0
answer_zero = 0
for i in range(n) :
    board.append(list(map(int, input().split())))

def checkAll(n, x_idx, y_idx) :
    global answer_minus1
    global answer_plus1
    global answer_zero

    temp = 0
    count_zero = 0
    for i in range(x_idx, n + x_idx) :
        for j in range(y_idx, n + y_idx) :
            temp += board[i][j]
            if (board[i][j] == 0) :
                count_zero += 1


    if count_zero == n ** 2:
        answer_zero += 1
        return True

    if temp == n**2 :
        answer_plus1 += 1
        return True

    elif temp == -(n**2) :
        answer_minus1 += 1
        return True

def divideCon(n, x_idx, y_idx) :
    global answer_minus1
    global answer_plus1
    global answer_zero

    if(checkAll(n, x_idx, y_idx)) : return True

    for i in range(3) :
        for j in range(3) :
            divideCon(n//3, x_idx + i*(n//3), y_idx + j * (n//3))


divideCon(n, 0, 0)

print(answer_minus1)
print(answer_zero)
print(answer_plus1)