from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
result = []
q = deque()

for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    for i in range(1, n + 1):
        if (indegree[i] == 0):
            q.append(i)

    while q:
        stu = q.popleft()
        result.append(stu)

        for i in graph[stu]:
            indegree[i] += -1
            if (indegree[i] ==  0):
                q.append(i)


topology_sort()

print(*result, sep=' ')