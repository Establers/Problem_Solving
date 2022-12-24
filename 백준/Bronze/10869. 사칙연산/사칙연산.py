import sys
a, b = map(int, sys.stdin.readline().rstrip().split())
print(f"{a+b}\n{a-b}\n{a*b}\n{int(a/b)}\n{a%b}")