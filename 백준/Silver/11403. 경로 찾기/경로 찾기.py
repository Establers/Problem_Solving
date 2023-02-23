import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

board = []
visited = [ [0] * n for _ in range(n) ]
canigo = [ [0] * n for _ in range(n) ]
for i in range(n) :
     board.append(list(map(int, input().split())))


def bfs2(v) :
    q = deque()
    q.append(v)
    node_check = [ 0 for _ in range(n)]

    while q:
        now = q.popleft() # 지금 밟은 노드

        for i in range(n) : # 이 노드에 대해서 모든 갈 수 있는 노드 조사
            if board[now][i] == 1 and node_check[i] == 0 :
                node_check[i] = 1
                canigo[v][i] = 1
                q.append(i)

for v in range(n) : # 모든 노드에 대해서
    bfs2(v)

for i in canigo :
    print(*i)