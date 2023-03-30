import sys
input = sys.stdin.readline

n = int(input()) # 추 개수
weight = [0] + list(map(int, input().split()))
# 확인하는 구슬의 크기가 인덱스를 벗어나는 경우가 있기에
# ss 를 40001로 고정한다.
# ss = sum(weight)
ss = 40001
# dp[i][j] : `i` 번째 무게를 사용할 때, `j`의 무게를 만들어 낼 수 있는지에 대한 것
dp = [
    [ 0 for _ in range(ss+1)]
    for _ in range(n+1)
]

# init
dp[0][0] = 1
for i in range(1, n+1) :
    for j in range(0, ss + 1) :
        # if dp[i][j] : continue
        if (j + weight[i]) <= ss :
            front = dp[i - 1][j + weight[i]]

        dp[i][j] = max(
            dp[i-1][j], # 밑으로 내려오는 경우
            dp[i-1][abs(j - weight[i])],
            front
        )


# print(*dp, sep='\n')
# print(dp[-1])
t = int(input())
tc = list(map(int, input().split()))
for check in tc :
    if dp[-1][check] == 1 :
        print("Y", end=' ')
    else :
        print("N", end=' ')