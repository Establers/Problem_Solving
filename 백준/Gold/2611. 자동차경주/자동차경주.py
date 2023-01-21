import sys
input = sys.stdin.readline
from collections import deque

# 모든 작업을 완료하기 위한 최소 시간 계산 
# 선행 관계 없는 작업들 동시 수행 가능?

n = int(input()) # 지점의 개수
graph = [ [] for i in range(n+1)]
indegree = [ 0 for i in range(n+1) ]
scores = [ 0 for i in range(n+1)] 
result= []
scores_res = [0] *(n+1)
route = [0] * (n+1)

m  = int(input()) # 간선 개수

for i in range(1, m+1) :
    a, b, c = (map(int ,input().split()))
    # 첫번쨰 입력이 1번
    # 출발 / 도착 / 점수
    graph[a].append( (b, c))
    indegree[b] += 1
    # scores[b] += c # 이 줄 자체가 잘못됐다. 
    # 간선에 대한 정보지, 각 노드에 대한 점수가 아니다...

def topology_sort() :
    global result
    q = deque()
    q.append(1) # 1번 노드부터 시작하니깐...
  
    for i in range(2, n+1) : 
        if indegree[i] == 0 :
            q.append(i)

    while q : 
        # print(q)
        now = q.popleft()
        
        if now == 1 and scores_res[1] != 0: 
            break
        
        result.append(now)
      
        for b, c in graph[now] : # 갈 노드, 간선 점수(커야 좋음)
            # print(graph[now])
            indegree[b] += -1
            if scores_res[b] < c + scores_res[now] : 
                scores_res[b] = c + scores_res[now]
                route[b] = now
                # 방문길을 최신화
                # b로 갈 간선은 now로...
            
            if indegree[b] == 0 : 
                q.append(b)
 
topology_sort()

route_list = [1] # 출발은 1번부터시작함.
i = 1
while True :
    if route[i] == 1 :
        route_list.append(1)
        break
    else :
        route_list.append(route[i])
        i = route[i]
      

print(scores_res[1])
print(*route_list[::-1])

"""
8
13
1 2 5
1 3 4
2 5 2
2 6 1
3 6 3
5 6 7
5 8 9
6 8 3
4 1 6
6 4 8
7 4 5
6 7 2
8 7 4
"""