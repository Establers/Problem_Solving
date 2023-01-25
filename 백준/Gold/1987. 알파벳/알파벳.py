import sys
from collections import deque
input = sys.stdin.readline

xx, yy = map(int, input().split())
graph = []
for i in range(xx) :
    graph.append(list(input().rstrip()))

dx = [-1, 1, 0,0]
dy = [0,0, -1, 1]
# 상 하 좌 우
count = 0

def bfs() :
    q = set()
#    global graph
    global count
    q.add((0, 0, graph[0][0])) # 초기 시작은 좌상단

    while q :
        x, y, now = q.pop()
        count = max(count, len(now))
        #print(now)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= xx or ny >= yy :
                continue
            else :
                if graph[nx][ny] not in now:
                    q.add((nx, ny, now+graph[nx][ny]))

bfs()
print(count)
