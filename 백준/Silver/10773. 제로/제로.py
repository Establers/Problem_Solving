from collections import deque

k = int(input())
queue = deque()
sum = 0
temp = 0
for i in range(k) :
    n = int(input())
    if n != 0 :
        queue.append(n)
    else :
        queue.pop()

for j in queue :
    sum += j

print(sum)

# print(sum(queue))