# 2606
import sys
input = sys.stdin.readline
from collections import deque

v = int(input())
e = int(input())
graph = [ [] for i in range(v+1)]
visited = [ 0 for _ in range(v+1)]

for i in range(1, e+1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
def bfs() :
    q = deque()
    q.append(1)

    while q :
        now = q.popleft()
        # print(now)
        # visited[now] = 1
        # if (graph[now]) :
        #     q.append(graph[now].pop())
        for i in graph[now] :
            if not visited[i]:
                q.append(i)
                visited[i] = 1

bfs()
#print(visited)
print(visited.count(1) - 1)


