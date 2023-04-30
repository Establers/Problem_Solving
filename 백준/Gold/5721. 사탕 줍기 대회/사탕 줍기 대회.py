import sys

input = sys.stdin.readline


def end_of_testcase(a, b):
    if a == 0 and b == 0:
        return True
    return False


# 0 0 입력 : 종료
while (True):
    m, n = map(int, input().split())
    if end_of_testcase(m, n): break

    # each 테스트 케이스
    a = [[0]]
    for _ in range(m):
        a.append(
            [0] + list(map(int, input().split()))
        )
    # print(a)
    # input end
    INT_MIN = float('-inf')
    dp_each_row = [ INT_MIN for _ in range(n+1)]
    dp_each_col = [ INT_MIN for _ in range(m+1)]
    # dp[i] : `i` 번째 까지 고려했을 때, 나올 수 있는 최대 값

    # 행부터 계산
    for i in range(1, m+1) :
        dp_each_row = [INT_MIN for _ in range(n + 1)]
        dp_each_row[1] = a[i][1]

        if n >= 2 :
            dp_each_row[2] = max(dp_each_row[1], a[i][2])

        for j in range(3, n+1) :
            dp_each_row[j] = max(dp_each_row[j-2] + a[i][j],
                                 dp_each_row[j-1])
        # print(dp_each_row)
        dp_each_col[i] = dp_each_row[n]

        if i >= 3 :
            dp_each_col[i] = max(dp_each_col[i-2] + dp_each_col[i],
                                 dp_each_col[i-1])

        elif i == 2 :
            dp_each_col[i] = max(dp_each_col[i], dp_each_col[i-1])

    print(dp_each_col[m])