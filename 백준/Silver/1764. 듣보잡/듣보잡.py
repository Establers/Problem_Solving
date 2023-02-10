import sys
input = sys.stdin.readline

n, m = map(int, input().split())# 듣도, 보도 수

dutdo = set()
bodo = set()

for i in range(n) :
    dutdo.add(input().rstrip())

for i in range(m):
    bodo.add(input().rstrip())

count = 0
result = []
if n < m :
    for str in dutdo :
        if str in bodo :
            count += 1
            result.append(str)

else :
    for str in bodo :
        if str in dutdo :
            count += 1
            result.append(str)

print(count)
result.sort()
print(*result, sep='\n')
