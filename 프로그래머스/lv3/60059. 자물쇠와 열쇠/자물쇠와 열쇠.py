n = 0
m = 0
answer = False

def key_rotation(board) : 
    next_board = [
        [0 for _ in range(m+1)]
        for _ in range(m+1)
    ]
    
    for i in range(m+1) :
        for j in range(m+1) :
            next_board[j][m+1-i-1] = board[i][j]
    
    return next_board
    

def key_lock_adder(sx, sy, plock, key, lock):
    global temp_lock 
    temp_lock = [
       [0 for _ in range(2*m + n + 1)]
        for _ in range(2*m + n + 1)
    ]
    
    for i in range(m, m+n+1) : # 2, 3, 4
        for j in range(m, m+n+1) : # 2, 3, 4
            temp_lock[i][j] = lock[i-m][j-m]

    
    for i in range(sx, sx + m+1) :
        for j in range(sy, sy+ m+1) :
            temp_lock[i][j] = plock[i][j] + key[i-sx][j-sy]

    return temp_lock

def key_lock_checker(lock) :
    for i in range(m, m+n+1) :
        for j in range(m, m+n+1) :
            if lock[i][j] == 2 or lock[i][j] == 0 :
                return False
            
    return True
    
    
def solution(key, lock):
    global m, n, answer
     
    
    m = len(key[0]) - 1     # 자물쇠
    n = len(lock[0]) - 1    # 열쇠
    print(n, m)
    
    """
    #1. lock 패딩 배열의 크기는 2*m + n + 1 임
    #2. 중간에 lock 원본 배열을 넣어야하는데 범위는 m ~ m+n 까지임
    #3. key를 0번 회전 했을 때 0~n 까지 탐색 한다. -> #5
    #4. key를 1, 2, 3번 회전 했을 때도 반복한다. -> #5
    
    #5. 패딩된 값을 복사한 빈 보드에, 값을 더한 뒤, lock에 해당하는 m ~ m+n 까지 인덱스를 검사한다.
    #6. 검사할 때, 2가 하나라도 있거나 0이 있다면 열 수 없다.
    #7. 만약 모두가 1 이라면 answer 에 True 값을 넣고 끝낸다.
    """
    
    #1
    padded_lock = [
        [0 for _ in range(2*m + n + 1)]
        for _ in range(2*m + n + 1)
    ]
    
    #2 
    for i in range(m, m+n+1) : # 2, 3, 4
        for j in range(m, m+n+1) : # 2, 3, 4
            padded_lock[i][j] = lock[i-m][j-m]
    

    def find() :
        global answer
        #3. 탐색 시작 인덱스
        for sx in range(0, n+m+1) :
            for sy in range(0, n+m+1) : 
                now_lock = key_lock_adder(sx, sy, padded_lock, key, lock)
                if key_lock_checker(now_lock) :
                    answer = True
                    return

    for _ in range(4) : # 0, 1, 2, 3
        if answer : break
        find()
        key = key_rotation(key)

    return answer 