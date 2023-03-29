import sys
input = sys.stdin.readline

n = int(input())
board = []

for _ in range(n) :
    board.append(list(map(int, input().split())))

dp = [
    [[0] * 3 for _ in range(n)]
    for _ in range(n)
]
# 0 : ㅡ
# 1 : |
# 2 : ＼
def init() :
    dp[0][1][0] = 1
    for i in range(2, n) :
        if board[0][i] == 0 :
            dp[0][i][0] = 1
        else :
            break

init()

for i in range(1, n) :
    for j in range(1, n) :
        if board[i][j] == 0 :
            dp[i][j][0] = dp[i    ][j - 1][0] + dp[i    ][j - 1][2]
            dp[i][j][1] = dp[i - 1][j    ][2] + dp[i - 1][j    ][1]

            if board[i-1][j-1] == 0 and board[i-1][j] == 0 and board[i][j-1] == 0 :
                dp[i][j][2] = dp[i - 1][j - 1][2] + dp[i - 1][j - 1][1] + dp[i-1][j-1][0]

print(dp[i][j][0] + dp[i][j][1] + dp[i][j][2])