import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
visited = [[0] * (n+1) for _ in range(h+2) ]
count = 0
flag = False
answer = int(1e9)
for i in range(m) :
    a, b = map(int, input().split())
    visited[a][b] = 1
    visited[a][b+1] = 2

# print(*visited, sep='\n')

def checking2(h_idx, n_idx, now) :
    if h_idx == h+2 :
        if now == n_idx :
            # print("제대로 도착", now, n_idx)
            return True
        else : return False
    # print(*visited, sep='\n')
  
    if(visited[h_idx][n_idx] == 1) :
        # 오른쪽 아래로
        #print("오 아")
        if(checking2(h_idx+1, n_idx+1, now)) :return True
    elif(visited[h_idx][n_idx] == 2):
        # 왼쪽 아래로
        #print("왼 아")
        if checking2(h_idx+1, n_idx-1, now) : return True
    else : # 0 일때 아래로
        #print("   아")
        if checking2(h_idx+1, n_idx, now) : return True

def checking3(h_idx, n_idx, now) : 
    while h_idx < h+2 :
        if visited[h_idx][n_idx] == 1 :
            h_idx += 1
            n_idx += 1
        elif visited[h_idx][n_idx] == 2 :
            h_idx += 1
            n_idx += -1
        else : 
            h_idx += 1
    if(n_idx == now) :
        return True
    else : return False
    

def bt(depth, a, b) : # 다리 놓기
    global answer
    global flag
    count = 0
    # print(depth)
    if depth == 4 : 
        return False
      
    for i in range(1, n+1) :
        if checking3(0,i,i) :
            count += 1
        else : break
    
    if count == n :
        # 만족하는 경우
        # print("끼얏호우")
        # print(depth)
        answer = min(answer, depth)
        flag = True
        # return True
  
    for i in range(1, h+1) :
        for j in range(b, n) :
            if(visited[i][j] == 0 and visited[i][j+1] == 0) :
                # 설치할 수 있는 곳
    
                # 배열 값 변경
                visited[i][j] = 1
                visited[i][j+1] = 2
                #print(*visited, sep='\n')
                if bt(depth + 1, i, j) : return True
                visited[i][j] = 0
                visited[i][j+1] = 0
            # 배열 값 복구
bt(0,1,1)
if flag : print(answer)
else : print(-1)