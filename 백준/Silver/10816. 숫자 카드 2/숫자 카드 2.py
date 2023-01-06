from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
queue = list(map(int, input().split()))

dict_1 = dict()
for i in queue :
    if i in dict_1 :
        dict_1[i] += 1
    else :
        dict_1[i] = 1

m = int(input())
queue2= deque()
queue2 = list(map(int, input().split()))

for i in queue2 :
    if i in dict_1 :
        print(dict_1[i], end=' ')
    else :
        print(0, end=' ')

# 시간 초과
