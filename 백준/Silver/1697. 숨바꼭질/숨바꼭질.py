import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100002
q = deque()

q.append(n)
visited[n] = True
day = 0

def bfs() :
    global day
    while q :
        length = len(q)

        while(length > 0) :
            length += -1
            now = q.popleft()
            # print(now)
            if now == k :
                print(day)
                return

            for i in (now-1, now+1, now*2) :
                if (0 <= i <= 100000 and not visited[i]) :
                    visited[i] = True
                    q.append(i)

        day += 1
bfs()