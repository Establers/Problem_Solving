import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v, e = map(int, input().split())
# 노드, 간선 개수

graph = [ [] for i in range(v+1) ]
visited = [ False for i in range(v+1) ]
# 간선에 대한 정보
for i in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



def dfs(a) :
    if visited[a] == False :
        visited[a] = True
        for i in graph[a] :
            dfs(i)
        return True
    return False

result = 0

for i in range(1, v+1) :
    if dfs(i) == True :
        result += 1

print(result)

