
import sys
input = sys.stdin.readline

num = int(input())
"""
prime_numlist = []

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

prime_numlist = prime_list(num) 
# print(prime_numlist)
# temp = [  for in range(2, num+1)]

result = []

for i in prime_numlist :
    if num % i == 0 : # 나눠진다면
        num = num // i
        result.append(i)
    if num < i :
        if (num == 1) : break
        if (result.)
        result.append(num)
        num = 1
    if num == 1 : break
print(len(result))
print(*result)
      
    """
result = []
for i in range(2, int(num**0.5)+1) :
    while (num % i == 0) :
        num = num / i
        result.append(i)
 #   if num % i == 0 :
  #      num = num / i
   #     result.append(i)

if num != 1 :
    result.append((int)(num))

result.sort()
print(len(result))
print(*result)