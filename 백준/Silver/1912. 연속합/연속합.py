import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int , input().split()))

dp = [ 0 for _ in range(n) ]

# init
dp[0] = a[0]
result = dp[0]


"""
ㅁ ㅁ  와, ㅁ `ㅁ` 비교
└───↑
dp[i] = max( dp[i-1] + a[i] , a[i] )
"""
for i in range(1, n):
    dp[i] = max( a[i] , dp[i-1] + a[i] )
    result = max(result, dp[i])

print(result)