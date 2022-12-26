import sys

list_square = list(map(int, sys.stdin.readline().split()))

list_square[2] = abs(list_square[0]-list_square[2])
list_square[3] = abs(list_square[1]-list_square[3])

print(min(list_square))