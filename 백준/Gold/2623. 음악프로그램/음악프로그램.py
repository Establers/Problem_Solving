import sys
input = sys.stdin.readline
from collections import deque

v ,e = map(int, input().split())
graph = [ [] for _ in range(v+1)]
indegree = [ 0 for _ in range(v+1) ]
result = []

for i in range(1, e+1) :
    list_ = list(map(int, input().split()))

    for j in range(1, len(list_)-1) :
        graph[list_[j]].append(list_[j+1])
        # print(list_[j+1])
        indegree[list_[j+1]] += 1
# print(indegree)
# print(graph)
flag_ = 0
count = 0
def topology_sort() :
    q = deque()
    global count
    for i in range(1, v+1) :
        if indegree[i] == 0 :
            q.append(i)

    while q :
        now = q.popleft() #
        count += 1
        result.append(now)

        for i in graph[now] :
            indegree[i] += -1

            if indegree[i] == 0 :
                q.append(i)


topology_sort()

if count == v :
    print(*result, sep='\n')
else :
    print(0)