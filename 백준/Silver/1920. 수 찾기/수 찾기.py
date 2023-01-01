import sys
input = sys.stdin.readline

n = int(input())
# _set = set()

_list = list(map(int, input().split()))
_set = set(_list)
# set이 list보다 검색 시간이 빠르다 해쉬어쩌고 그래서 set 형식으로 했고
# 또한 중복한 값을 제거해줘서 검색할 범위를 줄일 수 있음
m = int(input())
_mList = list(map(int, input().split()))
# 순서가 고려되는 요소이기에 set은 하지 않았음

for i in _mList : 
    print("1" if i in _set else "0")
    # 들어 있는지 확인하기 위해 in을 사용하였음.