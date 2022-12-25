import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, input().split()))
print("{} {}".format(min(num), max(num)))