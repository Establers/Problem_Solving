"""
weight 를 가진 최단 거리 -> 다익스트라

1. 직선도로는 결국 도로 전체 개수 - 1개 : 구하는 과정에서 고려하지 않고
맨 마지막에 -100원하면 될듯
2. 코너를 계산하는 방법
- 진행 방향이 바뀔 때 즉, dx dy의 방향이 바뀔 때 500원

또한 방향성이 있으니 dp ?.. 도 고려해볼 수 있겠다
"""
# 우선순위큐를 이용한 다익스트라
# (가격, x, y, dir)
import heapq

dx = [-1, 1, 0, 0] # 상 하 좌 우
dy = [0, 0, -1, 1] 
n = 0 

INT_MAX = float('inf')


def in_range(x,y) :
    global n 
    return 0 <= x < n and 0 <= y < n

def solution(board):
    # 보드 크기 25, 
    global n
    n = len(board)
    
    q = []
    
    distance = [
        [INT_MAX for _ in range(n)]
        for _ in range(n)
    ]

    heapq.heappush(q, (0, 0, 0, 3)) # 우
    distance[0][0] = 0
    # 초기 비용 0 
    
    while q :
        now_dist, x, y, now_dir = heapq.heappop(q)
        
        if now_dist != distance[x][y] :
            continue
        
        for next_dir in range(4) :
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]
            
            if not in_range(nx,ny) : continue   # 격자 외부
            if board[nx][ny] == 1 : continue    # 벽은 접근 불가
            
            # 갈 수 있는 공간
            # 만약 직전과 방향이 같다면
            if now_dir == next_dir : 
                if distance[x][y] + 100 < distance[nx][ny] : 
                    distance[nx][ny] = distance[x][y] + 100
                    q.append((distance[nx][ny], nx, ny, next_dir))
            
            # 다르다면
            elif now_dir != next_dir :
                if distance[x][y] + 500 + 100 < distance[nx][ny] :
                    distance[nx][ny] = distance[x][y] + 500 + 100
                    q.append((distance[nx][ny], nx, ny, next_dir))

    answer = distance[n-1][n-1]
    # 아래로 시작할 때
    # distance 초기화
    for i in range(n) :
        for j in range(n) :
            distance[i][j] = INT_MAX
            
    heapq.heappush(q, (0, 0, 0, 1)) # 아래
    distance[0][0] = 0
    # 초기 비용 0 
    
    while q :
        now_dist, x, y, now_dir = heapq.heappop(q)
        
        if now_dist != distance[x][y] :
            continue
        
        for next_dir in range(4) :
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]
            
            if not in_range(nx,ny) : continue   # 격자 외부
            if board[nx][ny] == 1 : continue    # 벽은 접근 불가
            
            # 갈 수 있는 공간
            # 만약 직전과 방향이 같다면
            if now_dir == next_dir : 
                if distance[x][y] + 100 < distance[nx][ny] : 
                    distance[nx][ny] = distance[x][y] + 100
                    q.append((distance[nx][ny], nx, ny, next_dir))
            
            # 다르다면
            elif now_dir != next_dir :
                if distance[x][y] + 500 + 100 < distance[nx][ny] :
                    distance[nx][ny] = distance[x][y] + 500 + 100
                    q.append((distance[nx][ny], nx, ny, next_dir))
            

    print(*distance, sep='\n')
    print(distance[n-1][n-1])
    answer = min(answer, distance[n-1][n-1])
    return answer
