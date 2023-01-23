import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

t = int(input()) # test case

def DFS(x, y) :
    if x <= -1 or x >= m or y <= -1 or y >= n :
        return False
    if graph[x][y] == 1 :
        graph[x][y] = 0
        DFS(x, y - 1)
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y + 1)
        return True
    return False

for _ in range(t) :
    result = 0
    m, n, k = map(int, input().split())
    # 가로 세로 배추개수
    graph = [ [0]*n for _ in range(m) ]

    # 그래프에 입력
    for i in range(k) :
        a, b = map(int, input().split())
        graph[a][b] = 1

    # print(graph)
    # DFS 수행
    for i in range(m) :
        for j in range(n) :
            if DFS(i,j) == True :
                result += 1

    print(result)


