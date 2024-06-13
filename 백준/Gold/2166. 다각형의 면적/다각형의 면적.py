import sys
input = sys.stdin.readline
# 외적
n = int(input())

xs = []
ys = []

for _ in range(n) :
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

# 마지막꺼 다시 추가
xs.append(xs[0])
ys.append(ys[0])

p = 0
m = 0

for i in range(n) :
    p += xs[i] * ys[i + 1]
    m += ys[i] * xs[i + 1]
    
answer = abs(p - m) / 2
print(answer)
