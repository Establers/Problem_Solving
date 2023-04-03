import sys
input = sys.stdin.readline

n = int(input())

board = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [ False for _ in range(n)]
    for _ in range(n)
]

dx = [1,-1, 0, 0]
dy = [0, 0, -1,1]

students = [[] for _ in range(n*n + 1)]
seq_stu = []

# 1 ~ 9
for _ in range(n*n):
    temp = list(map(int, input().split()))
    like = set(temp[1:])
    students[temp[0]].append(like)
    seq_stu.append(temp[0])
# 인풋 끝
# print(students[4])
# print(5 in students[4][0])
"""
# 1. 첫번째 학생부터 진행
# 2. 첫번째 학생을 for for로 배치
# 2.1 4방향에 대해 (좋아하는 친구 수, 비어있는 칸 수, -i, -j) 저장
# 2.2 다음 위치에서 다시 4방향에 대해 위를 구함
# 2.3 tuple 비교로 저것의 가장 큰 우선순위 값을 계속 가지고 있게함
# 2.4 비교가 다 끝났다면 남은 값의 i, j 로 첫번째 학생 배치 
"""
def in_range(x,y) :
    return 0 <= x < n and 0 <= y < n

# 1. 첫번째 학생부터 진행
# print(seq_stu)
for st in seq_stu :
    # 가장 우선순위가 낮은 값
    prev_case = (0, 0, -(n-1), -(n-1))
    my_x, my_y = n-1, n-1
    # 2. 첫번째 학생을 for for로 배치

    for i in range(n) :
        for j in range(n) :
            if board[i][j] != 0 : continue
            # 2.1 4방향에 대해 (좋아하는 친구 수, 비어있는 칸 수, -i, -j) 저장
            # 좋아하는 친구 수 계산, 빈칸 계산
            like_friend = 0
            empty_space = 0
            # 2.2 다음 위치에서 다시 4방향에 대해 위를 구함
            for k in range(4) :
                nx = i + dx[k]
                ny = j + dy[k]

                if in_range(nx, ny) :
                    if board[nx][ny] == 0 :
                        empty_space += 1
                    elif board[nx][ny] in students[st][0]:
                        like_friend += 1

            list_tuple = (like_friend, empty_space, -i, -j)
            if list_tuple > prev_case :
                # 2.3 tuple 비교로 저것의 가장 큰 우선순위 값을 계속 가지고 있게함
                my_x, my_y = -list_tuple[2], -list_tuple[3]
                # print(my_x, my_y)
                prev_case = list_tuple
            else :
                my_x, my_y = -prev_case[2], -prev_case[3]

    # 2.4 비교가 다 끝났다면 남은 값의 i, j 로 첫번째 학생 배치
    board[my_x][my_y] = st
#     print(board)
#
# print(board)
answer = 0
## 점수 계산 ##
for i in range(n) :
    for j in range(n) :
        now = board[i][j]
        cnt = 0
        for k in range(4) :
            nx = i + dx[k]
            ny = j + dy[k]

            if in_range(nx,ny) :
                if board[nx][ny] in students[now][0]:
                    cnt += 1
        if cnt != 0 :
            answer += 10**(cnt-1)

print(answer)