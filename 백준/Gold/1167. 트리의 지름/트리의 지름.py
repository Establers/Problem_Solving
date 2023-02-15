import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
visited = [ False for _ in range(n+1)]
graph = [ [] for _ in range(n+1)]
result = 0
edge_point = 0

for i in range(n) :
    input_list = list(map(int, input().split()))
    idx = 0
    p1 = input_list[0]
    # 1 2 , # 3 4
    while(True)  :
        a = input_list[idx+1]
        w = input_list[idx+2]
        graph[p1].append((a, w))  # (부모, 가중치)
        graph[a].append((p1, w))  # (자식, 가중치)
        idx += 2
        if (input_list[idx+1] == -1): break


def dfs(graph, visited, start, weight):
    global result
    global edge_point
    visited[start] = True

    for bb, cc in graph[start]:
        if not visited[bb]:
            weight = weight + cc
            if(weight > result) :
                result = weight
                edge_point = bb

            dfs(graph, visited, bb, weight)
            weight = weight - cc


dfs(graph, visited, 1, 0)
visited = [False for _ in range(n + 1)]
dfs(graph, visited, edge_point, 0)
print(result)
