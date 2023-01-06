from collections import deque
import sys
input = sys.stdin.readline
# push -> append
# pop
# size -> len
# empty : if queue : ..
# top : if queue : print[-1]
# sys.stdin.readline 안쓸 경우 , 시간초과 ?
# 
n = int(input())
queue = deque()
for i in range(n) :
    command = list(input().split())

    if command[0] == "push" :
        queue.append(int(command[1]))

    elif command[0] == "pop" :
        if queue :
            print(queue.pop())
        else :
            print("-1")

    elif command[0] == "size" :
        print(len(queue))

    elif command[0] == "empty" :
        if queue :
            print("0")
        else:
            print("1")

    elif command[0] == "top" :
        if queue :
            print(queue[-1])
        else :
            print("-1")


