import sys
input = sys.stdin.readline

n = int(input())
# _set = set()

_list = list(map(int, input().split()))
_set = set(_list)

m = int(input())
_mList = list(map(int, input().split()))

for i in _mList : 
    print("1" if i in _set else "0")