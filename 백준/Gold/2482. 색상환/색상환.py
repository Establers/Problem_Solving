n = int(input())
k = int(input())

dp = [
    [0 for _ in range(k+1)]
    for _ in range(n+1)
]
# dp[i][j] : `i` 번째 색상까지 고려했을 때, `j`가지를 고르는 경우의 수 누적
# 1~n, 1~k 사용

# init
for i in range(1, n+1) :
    dp[i][1] = i # 한개를 고르는 경우는 수

# dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
for i in range(2, n+1) :
    for j in range(2, k+1) :
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % (1_000_000_003)
        if i == n :
            dp[i][j] = (dp[n - 3][k - 1] + dp[n - 1][k]) % (1_000_000_003)

# 맨마지막의 경우, 첫번째꺼를 제외하고 고려해야하므로 n-2가 아니라 n-3
# print(*dp,sep='\n')
# answer = (dp[n-3][k-1] + dp[n-1][k]) % (1_000_000_003)
print(dp[n][k])