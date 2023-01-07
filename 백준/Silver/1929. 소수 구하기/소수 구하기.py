# M 이상 N 이하 소수 출력
import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())
if (M == 1) :
    M = 2
def check_prime(number) :
    for i in range(2, int(math.sqrt(number))+1) :
        if number % i == 0 :
            return False
    return True

for i in range(M, N+1) :
    if check_prime(i) == True :
        print(i)