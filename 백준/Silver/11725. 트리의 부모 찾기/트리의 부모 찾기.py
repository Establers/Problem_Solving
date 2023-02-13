import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [ [] for _ in range(n+1) ]
visited=  [ False for _ in range(n+1) ]
for i in range(n-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

p = [ 0 for _ in range(n+1) ]

#print(graph)
def bfs() :
    q = deque()
    q.append(1)
    visited[1] = True

    while q :
        now = q.popleft()
        for i in graph[now] :
            if visited[i] == False :
                p[i] = now # i의 부모노드는 now
                visited[i] = True
                q.append(i)

bfs()
print(*p[2:],sep='\n')