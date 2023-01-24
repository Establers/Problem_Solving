import sys
input = sys.stdin.readline
from collections import deque
#sys.setrecursionlimit(100000)

v, e = map(int, input().split())
# 노드, 간선 개수

graph = [ [] for i in range(v+1) ]
visited = [ False for i in range(v+1) ]
# 간선에 대한 정보
for i in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(a) :
    q = deque()
    q.append(a)
    visited[a] = True
    while q :
        now = q.popleft()
        for i in graph[now] :
            if visited[i] == False :
                q.append(i)
                visited[i] = True

result = 0

for i in range(1, v+1) :
    if visited[i] == False :
        if graph[i] :
            bfs(i)
            result += 1
        else :
            visited[i] = True
            result += 1

print(result)

