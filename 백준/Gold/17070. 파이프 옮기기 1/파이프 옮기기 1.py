import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = []

for i in range(n) :
    a = list(map(int, input().split()))
    graph.append(a)
board = [ [0]*n for _ in range(n) ]

dx = [0, 1, 1]
dy = [1, 0, 1]
# x +1 /  y+1   / x+1, y+1, (x+1,y+1) 점검 필요 암것도 없어야 이동가능
def dfs(x, y, status) :
    global result

    if x == n-1 and y == n-1 : # end 조건
        result += 1
        return
    # dx = [0, 1, 1]
    # dy = [1, 0, 1]
    if(status == 0) :
        if(x+1 < n and y+1 < n) :
            if (graph[x+1][y+1] != 1 and graph[x][y+1] != 1
                    and graph[x+1][y] != 1):
                dfs(x+1, y+1, 2)
        if (x < n and y+1 < n) :
            if (graph[x][y+1] != 1):
                    dfs(x, y+1, 0)
    if(status == 1) :
        if (x + 1 < n and y + 1 < n):
            if (graph[x + 1][y + 1] != 1 and graph[x][y + 1] != 1
                    and graph[x + 1][y] != 1):
                dfs(x + 1, y + 1, 2)
        if (x + 1 < n and y < n):
            if (graph[x + 1][y] != 1):
                dfs(x + 1, y, 1)

    if(status == 2) :
        if (x + 1 < n and y + 1 < n):
            if (graph[x + 1][y + 1] != 1 and graph[x][y + 1] != 1
                    and graph[x + 1][y] != 1):
                dfs(x + 1, y + 1, 2)
        if (x + 1 < n and y < n):
            if (graph[x + 1][y] != 1):
                dfs(x + 1, y, 1)
        if (x < n and y+1 < n) :
            if (graph[x][y+1] != 1):
                    dfs(x, y+1, 0)

#...............................................;;;;;;;;;


result = 0
if(graph[n-1][n-1] == 1) :
    print(0)
else :
    dfs(0,1,0)
    print(result)
#print(graph)



