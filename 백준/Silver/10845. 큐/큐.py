from collections import deque
import sys
input = sys.stdin.readline
# push -> append
# pop : 가장 앞에있는거라 popleft
# size -> len
# empty : if queue : ..
# front : print[0]
# back : pirnt[-1]
# sys.stdin.readline 안 쓸 경우, 시간초과

n = int(input())
queue = deque()
for i in range(n) :
    command = list(input().split())

    if command[0] == "push" :
        queue.append(int(command[1]))

    elif command[0] == "pop" :
        if queue :
            print(queue.popleft())
        else :
            print("-1")

    elif command[0] == "size" :
        print(len(queue))

    elif command[0] == "empty" :
        if not queue :
            print("1")
        else:
            print("0")

    elif command[0] == "back" :
        if queue :
            print(queue[-1])
        else :
            print("-1")

    elif command[0] == "front" :
        if queue :
            print(queue[0])
        else :
            print("-1")
