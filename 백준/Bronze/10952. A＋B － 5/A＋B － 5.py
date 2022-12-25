import sys

ans_list = []
# 값 담을 공간

while True : 
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if(a == 0 and b == 0) : break
    ans_list.append(a+b)
    
print(*ans_list, sep='\n')