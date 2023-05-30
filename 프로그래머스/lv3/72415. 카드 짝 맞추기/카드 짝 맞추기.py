from collections import deque

"""
1. 1,2,3 으로 모든 순열 경우의 수를 생성한다.
2. 해당 경우의 수로 BFS로 방문하며 최단거리
3. 답을 갱신해나간다
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 컨트롤 관리
# 엔터 관리
# 전체 횟수 관리 times -> min : answer

visited = [
    [False for _ in range(4)]
    for _ in range(4)
]


answer = int(2e9)
cards = { i : [] for i in range(1,7)}

able_cards = []
perm_cards = []

def solution(board, r, c):
    global answer, cards, able_cards, perm_cards
    # r : x , c : y 

    for i in range(4) :
        for j in range(4) :
            if board[i][j] != 0 :
                cards[board[i][j]].append((i, j))
    
    print(cards)
    # cards : 카드의 종류가 들어있음
    # {1: [(0, 0), (3, 2)], 2: [(1, 0), (2, 3)], 3: [(0, 3), (3, 0)], 4: [], 5: [], 6: []}
    
    for k, v in cards.items() : 
        if v != [] : 
            able_cards.append(k)

    print(able_cards)

    # 경우의 수 생성
    n = len(able_cards)
    card_visited = [ False for _ in range(n) ]
    permute(0, [], card_visited, n)

    print(perm_cards)
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    
    for pi in range(len(perm_cards)) :
        dfs(0, board, 0, pi, r, c)
    
    print(board)
   
    return answer

def dfs(depth, b, times, pi, sx, sy) : 
    global perm_cards, cards, answer
    
    if depth == len(able_cards) :
        answer = min(answer, times)
        # 카드개수만큼 enter 회수 추가
        return
    
    if times > answer :
        return 
    
    p = perm_cards[pi][depth] # [1, 2 ,3] 중 1 / 2 / 3
    # print(p)
    # a, b / b, a 순으로 가는게 있다. 둘 다 진행해서 맨마지막 결과를 보면 된다.
    t_c = cards[p] 
    # print("t_c :",t_c)
    # 1. a b 순으로 갈 때
    
    next_board = [
        [0 for _ in range(4)]
        for _ in range(4)
    ]
    
    for i in range(4) :
        for j in range(4) :
            next_board[i][j] = b[i][j]
            
    # print("전... pi :", pi, "depth :",depth)
    # print(*b, sep='\n')
    next_board[t_c[0][0]][t_c[0][1]] = 0
    next_board[t_c[1][0]][t_c[1][1]] = 0  
    
    # print("후.....")
    # print(*next_board, sep='\n')
    d1 = bfs(b, sx, sy, t_c[0][0], t_c[0][1]) # 시작점 -> a
    d2 = bfs(b, t_c[0][0], t_c[0][1], t_c[1][0], t_c[1][1]) # a -> b 
    dfs(depth + 1, next_board, times + d1 + d2 + 2, pi, t_c[1][0], t_c[1][1])
       
    # 1. b a 순으로 갈 때
    d3 = bfs(b, sx, sy, t_c[1][0], t_c[1][1]) # 시작점 -> b
    d4 = bfs(b, t_c[1][0], t_c[1][1], t_c[0][0], t_c[0][1]) # b -> a
    dfs(depth + 1, next_board, times + d3 + d4 + 2, pi, t_c[0][0], t_c[0][1])

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
    

def bfs(b, sx, sy, ex, ey) :
    q = deque() 
    
    dist = [
        [int(2e9) for _ in range(4)]
        for _ in range(4)
    ]

    q.append( (sx, sy) )
    dist[sx][sy] = 0
    
    while q :
        x, y = q.popleft()
        if x == ex and y == ey :
            return dist[ex][ey]
        
        for d in range(4) :
            nx = x + dx[d]
            ny = y + dy[d]

            if nx == x and ny == y : continue
            if not in_range(nx, ny) : continue
            # if dist[nx][ny] <= dist[x][y] + 1 : continue # 갈 곳이 작거나 같을 경우 굳이 거길 방문할 이유가 없다.
            if dist[nx][ny] > dist[x][y] + 1 :
                dist[nx][ny] = dist[x][y] + 1
                q.append( (nx, ny) )
        
        for d in range(4) :
            nx, ny = ctrl_move(b, x, y, d)
            
            if nx == x and ny == y : continue
            if not in_range(nx, ny) : continue
            # if dist[nx][ny] <= dist[x][y] + 1 : continue # 갈 곳이 작거나 같을 경우 굳이 거길 방문할 이유가 없다.
            if dist[nx][ny] > dist[x][y] + 1 :
                dist[nx][ny] = dist[x][y] + 1
                q.append( (nx, ny) )
                
    return dist[ex][ey]
    
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



    