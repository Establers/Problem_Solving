# 아기 상어 16236

import sys
input = sys.stdin.readline
from collections import deque
# 아기 상어 기본 크기 2,
# 크기 미만 인 것만 먹을 수 있음
# 지나 갈 순 있음

# 갈수 있는 공간 : 행동
#  0  : 도움
#  1  : 그 물고기 먹기
# 2,3 : "거리"가 가장 가까운? 먹이 먹기 복사그래프[도착지] - 복사그래프[출발지]?
# 만약 거리가 같음
# -> 제일 위에 있는([최소][])
# 그래도 2개이상 있다면, [최소][최소]
# 먹으면 자신의 크기 +1


dx = [1, -1, 0, 0]
dy = [0, 0,  1,-1]

N = int(input())
graph = []

# 맵 입력
for i in range(N) :
    ins = list(map(int, input().split()))
    graph.append(ins)

size_now = 2
x_now = 0
y_now = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x_now = i
            y_now = j
            graph[i][j] = 0

# 최단 거리 계산
def bfs() : #
    graph_dist = [ [-1 for i in range(N)] for _ in range(N)]
    graph_dist[x_now][y_now] = 0
    q = deque()
    q.append( (x_now, y_now))

    while q :
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N and 0 <= ny < N) == False :
                continue  # 못가는 공간
            elif (graph[nx][ny] <= size_now) and graph_dist[nx][ny] == -1 :
                # 상어 사이즈가 내 이하이고, 방문하지 않았다면
                graph_dist[nx][ny] = graph_dist[x][y] + 1
                q.append( (nx, ny) )

    return graph_dist


# print(bfs())

def find_eatable_fish(graph_dist) :
    x = 0
    y = 0
    dist_min = 1e9
    # for문 시작을 가장 위쪽, 가장 왼쪽에서 시작하므로 자동적으로 위,왼 조건 만족
    for i in range(N) :
        for j in range(N) :
            if graph_dist[i][j] != -1 and 1 <= graph[i][j] < size_now :
                # 먹을 수 있는 경우, 모든 경우 탐색
                # 가장 가까운 거리 찾기
                if graph_dist[i][j] < dist_min : # 미만으로 해야 위,왼 조건 가능
                    dist_min = graph_dist[i][j]
                    x, y = i, j # 먹을 물꼬기 위치..

    # 탐색 완료
    if dist_min == 1e9 :
        # 먹을게 없는 경우
        return None
    else :
        return (x, y, dist_min)
        # 먹을거 좌표, 최단거리 리턴


# main
result = 0
count_eat_fish = 0

while True :
    fihses = find_eatable_fish(bfs())
    if fihses is None : # 더 이상 먹을게 없다면
        print(result)
        break
    else :
        x_now, y_now = fihses[0], fihses[1]
        # 결국 출력은 움직인 거리임
        result += fihses[2]

        # 먹었으면 0으로 처리
        graph[x_now][y_now] = 0

        # 먹은 개수가 사이즈와 같다면 사이즈 증가
        count_eat_fish += 1
        if (count_eat_fish == size_now) :
            size_now += 1
            # 먹었던 개수 초기화
            count_eat_fish = 0


