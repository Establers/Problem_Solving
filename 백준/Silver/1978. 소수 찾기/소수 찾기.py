import sys
import math # sqrt
N = int(sys.stdin.readline().rstrip()) # 받을 수의 개수

list_num = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0 # 소수 개수 ++

# 1은 소수가 아니니 list_num에서 제거
if 1 in list_num :
    list_num.remove(1)

def issosu(number) :
    # 2 부터 모든 수에 대해서 진행해도 되지만
    # 소수 판별 방법이 그 수의 root 까지만 확인해도 됨
    for i in range(2, int(math.sqrt(number)) + 1) :
        if number % i == 0 :  # 어떤 수에 대해 나눠지면
            return False  # 소수가 아니니 False 리턴
    return True

for num in list_num : # 리스트에 포함된 num에 순서대로 접근
    # 소수 확인
    if (issosu(num) == True) : 
        cnt += 1

print(cnt)