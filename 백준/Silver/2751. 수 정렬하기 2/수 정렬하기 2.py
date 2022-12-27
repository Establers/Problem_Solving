import sys
# 수의 개수
n = int(sys.stdin.readline().rstrip())

list_ = []

for _ in range(n) : 
    list_.append(int(sys.stdin.readline().rstrip()))

list_.sort()

print(*list_, sep='\n')