import sys

N = int(sys.stdin.readline())
num  = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(num.count(v))