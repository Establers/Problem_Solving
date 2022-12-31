import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) : 
    _list = list(map(int, sys.stdin.readline().split()))
    avg = sum(_list) / 10
    print("#{} {}".format(i, avg))


