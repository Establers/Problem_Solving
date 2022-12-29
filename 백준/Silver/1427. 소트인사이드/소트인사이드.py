import sys
input = sys.stdin.readline

_list = input().rstrip()
_list = list(_list)
# print(_list)

_list.sort(reverse=True)

print(*_list, sep='')

