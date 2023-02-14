import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    for i in range(b) :
        input()
    print(a-1)