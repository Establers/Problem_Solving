import sys
input = sys.stdin.readline

# 보면 삼각형이라 3번안에 규칙이 나올 것 처럼 생겼음
# 1 1 1 2 2 3 4 5 7 9 12 16 21 ..
# d[n] = d[n-2] + d[n-3]

t = int(input())

d = [1] * (101)

for i in range(3, 101) :
    d[i] = d[i-2] + d[i-3]

for _ in range(t) :
    n = int(input())
    print(d[n-1])