import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
a, b = map(int, input().split())
e = int(input())
graph = [[0] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(e) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) # 무방향(양방향)

# bfs 함수 안쓰고 해버리기
q = deque()
q.append(a)
visited[a] = True
count = 0
answer = 0
while(q) :
    q_size = len(q)

    for i in range(q_size):
        now = q.popleft()
        if now == b :
            answer = count
            print(answer)
            exit()
        for k in graph[now] :
            if not visited[k] :
                q.append(k)
                visited[k] = True

    count += 1

if answer == 0 :
    print(-1)