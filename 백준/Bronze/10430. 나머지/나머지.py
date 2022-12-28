import sys

# 세 수 입력
a, b, c = map(int, sys.stdin.readline().split())

# 계산식
print((a+b)%c)
print(((a%c) + (b%c)) % c)
print((a*b)%c)
print(((a%c) * (b%c)) % c)