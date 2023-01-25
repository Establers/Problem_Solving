import sys
input = sys.stdin.readline

n = int(input())
dp = [ [0 for i in range(3)] for _ in range(1001)]

idx = 0
for i in range(n) :
    dp[i] = list(map(int, input().split()))
    
# 셋 중 하나를 선택하면 남은 두개중에 최소 값 선택을 계속 반복하면 됨
for i in range(1, n+1) :
    # RGB - R선택
    dp[i][0] = dp[i][0] + min(dp[i-1][1], dp[i-1][2])
    #G
    dp[i][1] = dp[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    #B
    dp[i][2] = dp[i][2] + min(dp[i - 1][1], dp[i - 1][0])

print(min(dp[n-1]))
