n = int(input())

dp = [ [0] * 10 for _ in range(101)]


"""
첫번째 경우인 1    2    3    4     5     6     7     8    9 에서 다음의 경우를 고려해보면
ㅇㅇㅇㅇㅇㅇ(1,0)(1,3)(2,4),(3,5),(4,6),(5,7),(6,8),(7,9),(8)
ㅇㅇㅇㅇㅇㅇ 0은 1. 9는 8 만 가능
"""

for i in range(1, 10) :
    dp[1][i] = 1

for i in range(2, n+1) :
    for j in range(10) : #0 ~ 9
        if (j == 0) :
            dp[i][j] = (dp[i-1][1])  % 1_000_000_000

        elif (1 <= j <= 8) :
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1_000_000_000

        else :
            dp[i][j] = (dp[i-1][8])  % 1_000_000_000

print(sum(dp[n]) % 1_000_000_000)