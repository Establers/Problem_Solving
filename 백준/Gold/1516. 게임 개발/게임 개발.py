import sys
from collections import deque
import copy
input = sys.stdin.readline

n = int(input())

graph = [ [] for _ in range(n+1)]
times = [0 for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]


for i in range(1, n+1) :
    list_ = list(map(int, input().split()))
    times[i] = list_[0]
    for j in list_[1: -1] :
        indegree[i] += 1
        graph[j].append(i)

result = copy.deepcopy(times)
def topology_sort() :
    q = deque()

    for i in range(n+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft()

        for i in graph[now] :
            result[i] = max(result[i], result[now] + times[i])
            indegree[i] += -1
            # result[i] = min(result[i], result[now] + times[i])

            if indegree[i] == 0 :
                q.append(i)

topology_sort()

print(*result[1:], sep='\n')
