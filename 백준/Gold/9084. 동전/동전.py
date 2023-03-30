import sys
input = sys.stdin.readline



t = int(input())

for _ in range(t) :
    n = int(input()) #동전 수

    # dp[i] = `i` 원을 만들 수 있는 방법의 개수

    coins = list(map(int, input().split()))
    m = int(input())
    dp = [0 for _ in range(m + 1)]
    dp[0] = 1

    # for i in range(coins[0]+1, m+1) :
    #     for j in range(n) :
    #         if i - coins[j] >= 0 :
    #             dp[i] = dp[i] + dp[i - coins[j]]

    # print(dp)

    for i in range(n) :
        for j in range(1, m+1) :
            if j - coins[i] >= 0 :
                dp[j] = dp[j] + dp[j - coins[i]]

    # print(dp)
    print(dp[m])





