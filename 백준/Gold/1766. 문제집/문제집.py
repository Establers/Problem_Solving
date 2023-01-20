# from collections import deque
import heapq
import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
graph = [ [] for _ in range(n+1)]
indegree = [ 0 for _ in range(n+1)]


# 입력 넣기
for i in range(1, m+1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

# print(graph)
# print(indegree)
result = []

def topology_sort() :
    q = []
    global result

    for i in range(1, n+1) :
        if indegree[i] == 0 :
            heapq.heappush(q, i)

    while q :
        # now = q.popleft()

        # now = min(q)
        # q.remove(now)
        now = heapq.heappop(q)

        result.append(now)
      # print(result)
        for i in graph[now] :
            indegree[i] += -1
            if indegree[i] == 0 :
                heapq.heappush(q, i)

topology_sort()

for i in result :
    print(i, end=' ')