import sys
# 수의 개수
n = int(sys.stdin.readline().rstrip())

list_ = set()
# 출력 조건이 중복 제거

for _ in range(n) : 
    list_.add(sys.stdin.readline().rstrip())

list_ = list(list_)

list_.sort()
list_.sort(key = len)

print(*list_, sep='\n')