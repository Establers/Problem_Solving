import sys
input = sys.stdin.readline

"""
N : 100,000
Q : 200,000
O(N * Q), O(N^2) .. 등 이런 류의 시간복잡도를 가지는 알고리즘은 제한 시간을 훨씬 초과하므로 사용 불가

미라 작업을 해두어 Q에 대해 바로 인덱스로 구할 수 있어야함.

(a+b+c) * (a+b+c)
= a^2 + b^2 + c^2 + 2(ab + bc + ca)
그러므로 우리가 구하고자하는 ab + bc + ca 는 위 값에서 추출할 수 있다
sum_a[r] - sum
"""

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

# 전처리
# 우리가 원하는 값은 각 누적합과 각각의 제곱들임

# 누적합
sum_a =  [0 for _ in range(n+1)]
sum_a[1] = a[1]
for i in range(2, n+1) :
    sum_a[i] = sum_a[i-1] + a[i]

# 제곱의 누적합을 구해야함
sqr_a = [0 for _ in range(n+1)]
for i in range(1, n+1) :
    sqr_a[i] = a[i]**2  # 파이썬에서의 제곱 표현임

sum_sqr_a = [0 for _ in range(n+1)]
sum_sqr_a[1] = sqr_a[1]
for i in range(2, n+1) :
    sum_sqr_a[i] = sum_sqr_a[i-1] + sqr_a[i]

# print(sum_a, sum_sqr_a)
for _ in range(q) :
    l, r = map(int, input().split())
    sum_gap = sum_a[r] - sum_a[l-1]
    sum_sqr_gap = sum_sqr_a[r] - sum_sqr_a[l-1]
    # print(sum_gap, sum_sqr_gap)
    ans = (sum_gap**2 - sum_sqr_gap)//2
    print(ans)