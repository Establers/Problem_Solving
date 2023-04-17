# dp로 변경 내용추적하기 귀찮으니
# bfs로 하자

from collections import deque

n = int(input())


visited = [False for _ in range(n+1)]
visited[n] = True
def bfs() :
    global visited
    q = deque()
    q.append((n, [n]))
    while q :
        now, li = q.popleft()
        # print(li)
        if now == 1 :
            # end
            print(len(li) - 1)
            print(*li)
            return

        if now % 3 == 0 :
            if not visited[now // 3] :
                q.append( (now // 3, li + [now // 3]) )
                visited[now // 3] = True

        if now % 2 == 0 :
            if not visited[now // 2]:
                q.append((now // 2, li + [now // 2]))
                visited[now // 2] = True

        if not visited[now - 1]:
            q.append((now - 1, li + [now - 1]))
            visited[now - 1] = True

bfs()