import sys
input = sys.stdin.readline
from collections import deque

v, e, start = map(int, input().split())
graph = [ [] for i in range(v+1) ]
visited = [False] *(v+1)
result = []

for i in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향이라서 추가

#print(graph)
def dfs(graph, v, visited) : 
    visited[v] = True
    result.append(v)

    graph[v].sort() # 최소값 부터 스택에 넣기 위해

    for i in graph[v] : 
        if visited[i] == False :
            dfs(graph, i, visited)

dfs(graph, start, visited)
print(*result, sep=' ')

result = []
visited = [False] *(v+1)

def bfs(graph, start, visited)  :
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q : 
        #print(q)
        now = q.popleft()
        
        # print(now)
        result.append(now) 
        
        visited[now] = True
        graph[now].sort() # 최소값부터 큐에 넣기 위해
        for i in graph[now] : 
            if visited[i] == False :
                q.append(i)
                visited[i] = True

bfs(graph, start, visited) 
print(*result, sep=' ')