import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
visited = [ False for _ in range(n+1)]
is_leap = [ False for _ in range(n+1)]
graph = [ [] for _ in range(n+1)]
result = 0
edge_point = 0
for i in range(n-1) :
    a, b, c = map(int, input().split()) # 부모, 자식, 가중치
    is_leap[a] = True
    graph[b].append((a, c)) # (부모, 가중치)
    graph[a].append((b, c))  # (자식, 가중치)

# print(graph)
# print(graph[2])


def dfs(graph, visited, start, weight):
    global result
    global edge_point
    visited[start] = True

    # weight += graph[start][1]
    # result = max(result, weight)

    for bb, cc in graph[start]:
        if not visited[bb]:
            # print("wegiht = ",weight, " + ", cc)
            weight = weight + cc
            if(weight > result) :
                result = weight
                edge_point = bb


            dfs(graph, visited, bb, weight)
            weight = weight - cc

# for idx in range(1, n+1) :
#     if is_leap[idx] is False :
#         print(idx, "를 서칭합니당..")



dfs(graph, visited, 1, 0)
# print(edge_point)
visited = [False for _ in range(n + 1)]
# print("dsadasd")
dfs(graph, visited, edge_point, 0)
print(result)
