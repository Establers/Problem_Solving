import sys
input = sys.stdin.readline

_list = []

N = int(input())
for i in range(N) :  
    xy = list(map(int, input().split()))
    # 받는 것을 [x, y] 리스트 형식으로
    _list.append(xy)

# 다 받았을 경우
  
# _list.sort(key= lambda x : x[1])
# 문제점 : x[0] 에 대한 정렬은 보장할 수 없음.

_list.sort(key= lambda x : (x[1], x[0]))
# 두개를 다 쓰면 된다..!..
for j in _list : 
    print(*j)