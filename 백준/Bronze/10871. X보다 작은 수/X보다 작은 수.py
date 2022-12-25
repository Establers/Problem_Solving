import sys

N, X= map(int,sys.stdin.readline().split())

num  = list(map(int, sys.stdin.readline().split()))

for i in range(N) :
    if num[i] < X :
        print(num[i], end=' ')