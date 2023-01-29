# 아기상어 복습
import sys
input = sys.stdin.readline
from collections import deque
N = int(input())

graph = []

for i in range(N) :
    li = list(map(int, input().split()))
    graph.append(li)

# 상하 좌우를 위한 dx dy
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 9의 위치를 찾아내기
now_x = 0
now_y = 0
for i in range(N) :
    for j in range(N) :
        if graph[i][j] == 9 :
            now_x = i
            now_y = j
            graph[now_x][now_y] = 0
            # 나는 시작지점이고 방문이 가능한 곳이니 0으로 해야함 
            # 이걸 빼먹어서 값이 이상하게 나왔음

now_size = 2 # 현재 상어의 사이즈

# 최단 거리를 수시로 구해야할 것 처럼 보인다.
# 먹을 물고기를 찾기 위해서 최단 거리가 들어있는 배열을 구해야함
# bfs로 특정 지점에 해당하는 거리를 찾을 수 있음 이 배열을 구해보자..
def bfs() : # return : graph_dist [N][N] 전체
    # 우선 graph를 손상시키지 않고, 거리만 있는 배열을 구해야하기에
    # 새롭게 배열을 만든다
    graph_dist = [ [-1 for _ in range(N)] for _ in range(N)]

    # 이 배열에 현재위치에서 특정 위치로의 최단 거리를 구해기 위해
    # 현재 위치 정보를 0으로 넣어준다 (for 최단거리 1움직이면 1로 설정하기 위해)
    graph_dist[now_x][now_y] = 0
    # 그러면 bfs를 수행했을 때 특정위치 까지 거리를 구할 수 있게 된다.

    # bfs를 수행해보자
    q = deque()
    q.append((now_x, now_y)) # 시작 값을 넣어준다.

    while q :
        x, y = q.popleft()

        for i in range(4) : # dx dy technique
            nx = x + dx[i]
            ny = y + dy[i]
            # 새로운 위치가 배열을 벗어나지 않을 경우 :
            if ( 0 <= nx < N and 0 <= ny < N) == True :
                # 상어의 사이즈 또한 고려를 해줘야 한다.
                # 나의 상어 사이즈가 이상일 경우 방문할 수 있다.
                #
                if (now_size >= graph[nx][ny]) : # 상어크기는 graph에 있다.
                    # 또한 방문 여부를 체크해야한다.
                    if (graph_dist[nx][ny] == -1) :# 이때까지 방문하지 않았을 경우
                        graph_dist[nx][ny] = graph_dist[x][y] + 1
                        # 거리를 1 늘려준다.
                        q.append((nx, ny))
                        # 다시 움직인 좌표를 q에 넣어준다

    # 거리를 구하는 작업이 끝나면 최단 거리가 있는 배열을 Return 한다.
    # print (graph_dist)
    return graph_dist
"""
[-1, 3, 2, 3], 
[3, 2, 1, 2], 
[2, 1, 0, 1], 
[3, 2, 1, -1]
"""
# 최단 거리 물고기를 찾아가서 먹으러 간다
def find_eatable_fish(graph_dist) :
    # 최단 거리 배열을 받은 후 이것을 기준으로 행동을 해야한다.
    
    # 최단 거리를 구하기 위해 임시값 설정
    shortest_dist = 1e9
    x, y = 0, 0
    
    # 진짜로 먹을 물고기를 탐색해보자..
    # 가장 위, 가장 왼쪽에서 부터 탐색하므로, 중복 될 경우 "<" 이기에, 값이 바뀌지 않고
    # 자연스럽게 가장 위, 가장 왼쪽 값으로 셋팅이 된다.
    for i in range(N) :
        for j in range(N) :
            # 방문을 할 수 있는 곳이고 ( -1 이면 나 보다 쌘 상어있어서 못감)
            # if (graph_dist[i][j] != -1) :
            # 물고기를 먹을 수 있는 사이즈라면 (graph[][])
            if (1 <= graph[i][j] < now_size) and (graph_dist[i][j] != -1) :
                # 만약 내가 가진 shortest_dist 보다 짧다면 (graph_dist[][])
                if (graph_dist[i][j] < shortest_dist) :
                    # 값을 갱신
                    shortest_dist = graph_dist[i][j]
                    # 추가로 그 위치를 알아야 먹으러 갈 수 있다. 저장해주자.
                    x, y = i, j

    # 만약 먹을 수 있는 물고기가 하나도 없다면 shortest_dist 는 갱신이 안된다.
    if (shortest_dist == 1e9) :
        return None # None 리턴으로 더이상 먹을게 없다는 것을 알려주자
    else :
        # 다 구했다면 위치랑, 거리를 리턴해주자
        return (x, y, shortest_dist)

# 이제.. 먹어봅시다..
# Main

result = 0 # 출력할 결과 값
eat_count = 0 # 먹은 물고기 개수
# 먹을 물고기 선택하기
while True : # 더이상 먹을게 없을 때 까지 반복해야한다.
    fish = find_eatable_fish(bfs())
    # print(fish)
    if fish is None :
        # 종료조건
        print(result)
        break
    else :
        now_x = fish[0]
        now_y = fish[1]
        # 이걸 빼먹어서 자리가 계속 고정인 채로 있었음 영혼이 보내서 먹고온것...
        # 먹으러 갑시당...
        graph[now_x][now_y] = 0 # 냠 .. 먹었으니 0
        result += fish[2] # 거리 더하기 누적

        # 먹었으니 먹은 개수 count 증가
        eat_count += 1
        # 아기상어의 성장
        if (eat_count == now_size) :
            now_size += 1
            eat_count = 0 # 성장했으니 다시 먹은 개수 초기화

