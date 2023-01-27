from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [ [] for i in range(n+1) ]
indegree = [0 for i in range(n+1)]
result = []
q = deque()

for i in range(1, m+1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    for i in range(1, n+1) : # 진입 차수 0 인것 큐에 넣기
        if (indegree[i] == 0) :
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now] :
            indegree[i] += -1 # 진입 차수 감소
            if(indegree[i] == 0) : # 다시 0 이면 큐에 추가
                q.append(i)

topology_sort()
print(*result, sep=' ')