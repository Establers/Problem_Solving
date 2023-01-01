import sys
input = sys.stdin.readline

_list = []

N = int(input())
for i in range(N) :  
    xy = list(map(int, input().split()))
    # 받는 것을 [x, y] 리스트 형식으로
    _list.append(xy)

# 다 받았을 경우

_list.sort()
for j in _list : 
    print(*j)