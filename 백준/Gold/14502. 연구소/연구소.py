import sys
input = sys.stdin.readline
import copy
from collections import deque

n, m = map(int, input().split())
graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

for i in range(n) :
    graph.append(list(map(int, input().split())))

# print(graph)

# 1. 임의점 3곳을 선정해 1로 하기
# 1-1 copy - 벽3개 선정 - bfs로 던져주기
def backtracking(depth, graph) :
    if (depth == 3) :
        bfs(graph)
        return
    else :
        for i in range(n) :
            for j in range(m) :
                if graph[i][j] == 0 :
                    graph[i][j] = 1
                    backtracking(depth+1, graph)
                    graph[i][j] = 0


# 2. 2의 위치마다 bfs 수행 (0 -> 2로 변경)
def bfs(graph) :
    graphTemp = copy.deepcopy(graph)
    #원형보존..
    #print(graphTemp)
    global result

    q = deque()
    for i in range(n) :
        for j in range(m) :
            if graphTemp[i][j] == 2 :
                q.append((i, j))

    while q :
        x, y = q.popleft()

        for k in range(4) :
            nx = x + dx[k]
            ny = y + dy[k]

            if (0 <= nx < n and 0 <= ny <m) :
                if(graphTemp[nx][ny] == 0) :
                    q.append((nx, ny))
                    graphTemp[nx][ny] = 2 #

    # 3. bfs q가 비어진 이후 n by m 에 대해 0의 개수를 count
    temp = 0
    #print(graphTemp)
    for a in graphTemp :
        temp += a.count(0)
        #print(temp)
    # 4. 0 개수가 크면 갱신
    result = max(result, temp)

backtracking(0, graph)
print(result)
