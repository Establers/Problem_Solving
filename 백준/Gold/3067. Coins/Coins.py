import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t) :
    n = int(input()) #동전의 가지수 # 1 ~ 20
    coins = list(map(int, input().split())) # 오름차순 해줌 다행히
    money = int(input()) # 1 ~ 10000

    dp = [0] * (money+1)
    dp[0] = 1
    for don in coins :
        for n in range(don, money + 1) : # money+1 미만 까지 -> money까지 접근
            dp[n] = dp[n] + dp[n - don]
            # print(dp)
            # if(dp[1] == 22) :
            #     print(don, n, money)

    print(dp[money])