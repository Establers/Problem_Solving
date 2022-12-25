import sys

x = int( sys.stdin.readline().rstrip())
# 횟수 입력 받기
ans_list = []
# 값 담을 공간?

for x in range(1, x+1) : # 횟수 만큼
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ans_list.append(a+b)
    
print(*ans_list, sep='\n')