import sys
input = sys.stdin.readline

n, k = map(int, input().split())
moneys = []

for i in range(n) :
    a = int(input())
    if a <= k :
        moneys.append(a)

result = 0

for i in moneys[::-1] :
    if k < i : continue
    else :
        temp = (int)(k/i)
        k = k - (i*temp)
        result += temp

print(result)

