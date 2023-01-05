import sys
input = sys.stdin.readline

a, b = map(int, input().split())
value = 0

for i in range(1,max(a,b)+1) :
    if a % i == 0 and b % i == 0 :
        value = i

print(value)
print(int(a*b / value))


