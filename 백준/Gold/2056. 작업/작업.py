import sys
input = sys.stdin.readline
import copy
from collections import deque

# 모든 작업을 완료하기 위한 최소 시간 계산 
# 선행 관계 없는 작업들 동시 수행 가능?

n = int(input())
graph = [ [] for i in range(n+1)]
indegree = [ 0 for i in range(n+1) ]
times = [ 0 for i in range(n+1)] 
result= []


for i in range(1, n+1) :
    list_ = list(map(int ,input().split()))
    # 첫번쨰 입력이 첫번째 작업
    # 시간 / 선행작업개수 / 선행 작업들
    times[i] = list_[0]
    for a in list_[2:] :
        graph[a].append(i)
        # a 를  해야  i 를 할 수 있음.
        indegree[i] += 1
          
result = copy.deepcopy(times) 
# print(graph)
# print(indegree)
def topology_sort() :
    q = deque()
    
    for i in range(1, n+1) :
        if indegree[i] == 0 :
            q.append(i)
            
    while q : 
        now = q.popleft()
      
        for i in graph[now] :       
            result[i] = max(result[i], result[now] +times[i])
            indegree[i] += -1
            if indegree[i] == 0 :
                q.append(i)
                
                
topology_sort()
print(max(result))
    
        