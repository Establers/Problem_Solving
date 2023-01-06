from collections import deque

a, b = map(int, input().split())
# queue = deque()
queue = deque([ i for i in range(1,a+1) ])

print("<",end='')
count = 0
while queue :
    for j in range(b-1) :
        queue.append(queue.popleft())
    temp = queue.popleft()
    print(temp, end='')
    count += 1
    if count < a :
        print(", ",end='')

print(">")