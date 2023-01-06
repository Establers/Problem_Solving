from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for i in range(n) :
    command = list(input().split())

    if command[0] == "push_back" :
        queue.append(int(command[1]))

    if command[0] == "push_front" :
        queue.insert(0, int(command[1]))

    elif command[0] == "pop_front" :
        if queue :
            print(queue.popleft())
        else :
            print("-1")

    elif command[0] == "pop_back" :
        if queue :
            print(queue.pop())
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
