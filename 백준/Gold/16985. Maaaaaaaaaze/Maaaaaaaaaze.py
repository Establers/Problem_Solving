import sys
input = sys.stdin.readline
from collections import deque
import itertools

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(rotated_graph) :
    q = deque()
    if rotated_graph[0][0][0] == 0 or rotated_graph[4][4][4] == 0 :
        return

    else :
        visited = [[[False] * 5 for i in range(5)] for _ in range(5)]
        distance = [[[0] * 5 for i in range(5)] for _ in range(5)]

        q.append((0,0,0))

    while q :
        z, x, y = q.popleft()

        for i in range(6) :
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if(0<=nx<5 and 0<=ny<5 and 0<=nz<5) :
                if(rotated_graph[nz][nx][ny] != 0) :
                    if not visited[nz][nx][ny] :
                        visited[nz][nx][ny] = True
                        distance[nz][nx][ny] = distance[z][x][y] + 1
                        q.append((nz, nx, ny))

    if distance[4][4][4] != 0 :
        answer.append(distance[4][4][4])


def rotation(n, li : list) :
    ret = [ [0] * 5 for _ in range(5)]
    # n * 90도 만큼 회전
    if n % 4 == 1 :
        for r in range(5) :
            for c in range(5) :
                ret[c][5-1-r] = li[r][c]

    elif n % 4 == 2 :
        for r in range(5):
            for c in range(5):
                ret[5-1-r][5-1-c] = li[r][c]

    elif n % 4 == 3 :
        for r in range(5) :
            for c in range(5) :
                ret[5-1-c][r] = li[r][c]

    else :
        for r in range(5) :
            for c in range(5) :
                ret[r][c] = li[r][c]

    return ret

board = [ [] for i in range(5) ]
graph = [[[0] * 5 for _ in range(5)] for _ in range(5)]
answer = []

for i in range(25) :
    temp = list(map(int, input().split()))
    board[i//5].append(temp)

for order in itertools.permutations([0,1,2,3,4], 5) :
    for i in range(5) :
        graph[order[i]] = board[i]

    rotated_graph = [[[0] * 5 for _ in range(5)] for _ in range(5)]

    for a in range(4) :

        for b in range(4) :

            for c in range(4) :

                for d in range(4) :

                    for e in range(4) :
                        rotated_graph[0] = rotation(a, graph[0])
                        rotated_graph[1] = rotation(b, graph[1])
                        rotated_graph[2] = rotation(c, graph[2])
                        rotated_graph[3] = rotation(d, graph[3])
                        rotated_graph[4] = rotation(e, graph[4])
                        #print(e, *rotated_graph[4], sep='\n')
                        # print(a,b,c,d,e)
                        bfs(rotated_graph)

if answer :
    ans = min(answer)
    print(ans)
else :
    print(-1)
