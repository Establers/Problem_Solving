# 정수 삼각형
import sys
input = sys.stdin.readline

n = int(input()) # 라인 수
d = []

"""
1
2 3
4 5 6
7 8 9 10
"""
for i in range(n) :
    numList = list(map(int, input().split()))
    d.append(numList)

for i in range(1,n) :
    for a in range(len(d[i])) : # 해당 라인의 숫자 수 만큼 반복
        if a == 0 : # 1자로 내려오는 경우
            d[i][a] += d[i-1][a]
        elif a == i : # 맨오른 쪽 값
            d[i][a] += d[i-1][a-1]
        else :
            d[i][a] += max(d[i-1][a-1], d[i-1][a])

print(max(d[-1]))