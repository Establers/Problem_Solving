import sys
sys = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))

dp = [1] * (n+1)


for i in range(n) :
    for j in range(i) :
        if numList[i] > numList[j] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))