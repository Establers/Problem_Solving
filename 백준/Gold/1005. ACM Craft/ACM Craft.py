import sys
input = sys.stdin.readline
from collections import deque

t = int(input()) # Tc
INT_MIN = float('-inf')
for _ in range(t) :
    n, k = map(int, input().split()) # 건물수, 규칙 수

    times = [0] + list(map(int, input().split()))
    # 각 건무를 짓는데 걸리는 시간 idx
    dp = [ -1 for _ in range(n+1)]

    # 풀이에 필요한 배열
    indegree = [ 0 for _ in range(n+1)]
    graph = [
        []
        for _ in range(n+1)
    ]

    for _ in range(k) :
        a, b = map(int, input().split()) # 건물 짓는 순서 a -> b
        graph[a].append(b)
        indegree[b] += 1

    target = int(input())

    q = deque()

    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
            dp[i] = times[i]
    # print(graph)
    while q :
        now_node = q.popleft()

        # 연결된 노드 중에서 가장 긴 시간을 저장하게함
        # 이게 결국 이게 되어야 하기에.
        for next_node in graph[now_node] :
            dp[next_node] = max(
                dp[next_node],
                dp[now_node] + times[next_node]
            )
            indegree[next_node] += -1

            if indegree[next_node] == 0 :
                q.append(next_node)

    print(dp[target])