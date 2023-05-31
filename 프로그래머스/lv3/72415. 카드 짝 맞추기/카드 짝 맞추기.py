from collections import deque

"""
1. 1,2,3 으로 모든 순열 경우의 수를 생성한다.
2. 해당 경우의 수로 BFS로 방문하며 최단거리
3. 답을 갱신해나간다
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



answer = int(2e9)
cards = { i : [] for i in range(1,7)}

able_cards = []
perm_cards = []

def solution(board, r, c):
    global answer, cards, able_cards, perm_cards

    for i in range(4) :
        for j in range(4) :
            if board[i][j] != 0 :
                cards[board[i][j]].append((i, j))
    
    print(cards)
    # cards : 카드의 종류가 들어있음
    # {1: [(0, 0), (3, 2)], 2: [(1, 0), (2, 3)], 3: [(0, 3), (3, 0)], 4: [], 5: [], 6: []}
    
    # 가능한 카드 종류를 가져오기 위해 key 값을 리스트로 저장함
    for k, v in cards.items() : 
        if v != [] : 
            able_cards.append(k)
            
    # 방문하는 방법의 모든 경우의 수는 순열
    # 순열 생성
    n = len(able_cards)
    card_visited = [ False for _ in range(n) ]
    permute(0, [], card_visited, n)

    # print(perm_cards)
    # 생성한 순열 결과 : [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    # 모든 경우의 수에 대해 시작지점에서 부터 DFS를 진행하며 답을 찾아간다.
    for pi in range(len(perm_cards)) :
        dfs(0, board, 0, pi, r, c)
    
    return answer

def dfs(depth, b, times, pi, sx, sy) : 
    global perm_cards, cards, answer
    
    # 현재 진행하고 있는 DFS가 답이 될 수 없는 구조라면 return 으로 끝낸다. (가지치기)
    if times >= answer :
        return
    
    # 현재 진행이 끝난 DFS가 정답이 될 수 있으면 갱신한다.
    if depth == len(able_cards) :
        answer = min(answer, times)
        return

    p = perm_cards[pi][depth] # [1, 2 ,3] 중 1 / 2 / 3
    # a, b / b, a 순으로 가는게 있다. 둘 다 진행해서 맨마지막 결과를 보면 된다.
    
    t_c = cards[p] 
    # print("t_c :",t_c)
    
    # 원본 보드를 훼손을 막기 위해
    # 새로운 보드를 만들어서 값을 넣는다.
    next_board = [
        [0 for _ in range(4)]
        for _ in range(4)
    ]
    
    for i in range(4) :
        for j in range(4) :
            next_board[i][j] = b[i][j]
    
    # 방문할 카드를 next_board 에서 미리 0으로 만들어 둔다. 
    next_board[t_c[0][0]][t_c[0][1]] = 0
    next_board[t_c[1][0]][t_c[1][1]] = 0  
    
    # 1. a b 순으로 갈 때
    d1 = bfs(b, sx, sy, t_c[0][0], t_c[0][1]) # 시작점 -> a
    d2 = bfs(b, t_c[0][0], t_c[0][1], t_c[1][0], t_c[1][1]) # a -> b 
    dfs(depth + 1, next_board, times + d1 + d2 + 2, pi, t_c[1][0], t_c[1][1])
    # 다시 dfs 를 진행한다.
    # times 에 + 2를 더하는 이유는 카드를 엔터를 두번하기 때문에 +2 를 하였음
    
    # 2. b a 순으로 갈 때
    d3 = bfs(b, sx, sy, t_c[1][0], t_c[1][1]) # 시작점 -> b
    d4 = bfs(b, t_c[1][0], t_c[1][1], t_c[0][0], t_c[0][1]) # b -> a
    dfs(depth + 1, next_board, times + d3 + d4 + 2, pi, t_c[0][0], t_c[0][1])
    # 다시 dfs 를 진행한다.

    
# 순열을 생성하기 위한 함수
def permute(depth, arr, visited, n) :
    global perm_cards, able_cards
    
    if depth == n :
        perm_cards.append(arr[:])
        return
    
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            arr.append(able_cards[i])
            
            permute(depth+1, arr, visited, n) 
            
            visited[i] = False
            arr.pop()
    
# 최단 거리를 구하기 위한 BFS
def bfs(b, sx, sy, ex, ey) :
    q = deque() 
    
    dist = [
        [int(2e9) for _ in range(4)]
        for _ in range(4)
    ]
    # 최단 거리를 구하기 위한 배열

    # 초기 시작 위치를 넣는다.
    q.append( (sx, sy) )
    dist[sx][sy] = 0
    
    while q :
        x, y = q.popleft()
        if x == ex and y == ey :
            return dist[ex][ey]
            # 도착지에 도달 하였다면 최단거리를 return 후 종료한다.
        
        # 일반 4방향에 대해 q에 값을넣는다.
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if nx == x and ny == y : continue
            if not in_range(nx, ny) : continue
            if dist[nx][ny] > dist[x][y] + 1 :
                dist[nx][ny] = dist[x][y] + 1   # 최단거리를 갱신할 수 있을 때 갱신해준다.
                q.append( (nx, ny) )
        
        for d in range(4) :
            # Ctrl 를 누른 채 움직이는 경우의 위치도 Q에 넣어준다.
            nx, ny = ctrl_move(b, x, y, d)
            
            if nx == x and ny == y : continue
            if not in_range(nx, ny) : continue
            if dist[nx][ny] > dist[x][y] + 1 :
                dist[nx][ny] = dist[x][y] + 1   # 최단거리를 갱신할 수 있을 때 갱신해준다.
                q.append( (nx, ny) )
                
    return dist[ex][ey]

# CTRL 을 누르면서 이동할 때, 그 이동할 위치 좌표를 리턴하는 함수
def ctrl_move(board, x, y, d) :  
    nx = x
    ny = y
    for _ in range(4) :
        nx = nx + dx[d]
        ny = ny + dy[d]
        
        if in_range(nx,ny) and board[nx][ny] != 0 : # card
            return (nx, ny)
        
        if not in_range(nx, ny) : 
            return (nx-dx[d], ny-dy[d])
        

def in_range(x, y) :
    return 0 <= x < 4 and 0 <= y < 4



    