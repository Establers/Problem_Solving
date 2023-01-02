# 0 1 1 3 2
# insert

line = []
n = int(input())
number = list(map(int, input().split()))

for i in range(n) :
    line.insert(i-number[i],i+1)
    # 뒤에서 인덱스를 해야하니...

print(*line)

