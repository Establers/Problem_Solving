import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# 냄새의 크기 K
board = []
total_count = M
times = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 0상, 1 아래 2 왼 3 오
for _ in range(N) :
    board.append(list(map(int, input().split())))

# 보드 입력 완료
shark = []

for i in range(N) :
    for j in range(N) :
        if board[i][j] != 0 :
            shark.append([board[i][j] - 1, i, j]) # 상어 : [등수 번호, x, y]

shark.sort()
# 상어에 대한 인덱스 넣음

# 상어에 대한 방향(각각의 방향)

seq = list(map(int, input().split()))
for i in range(len(seq)) :
    seq[i] += -1

for i in range(len(seq)) :
    shark[i].append(seq[i])

# 각 상어별 우선 순위
check_dir = []
for rank in range(M) :
    temp_list = []

    for a in range(4) :
        li = list(map(int, input().split()))
        # 인덱스 매치을 위한 1 감소
        for i in range(4) :
            li[i] = li[i] - 1
        temp_list.append(li)

    check_dir.append(temp_list)
#
# print(*check_dir,sep = '\n')

# 1. 냄새를 모두 1씩 줄이는 함수 굳이 안만들어도 될듯
# next_board : 상어의 다음위치를 저장해놓
# smell_board : 상어의 냄새의 K를 저장해놓
# smell_id_board : 상어의 냄새의 ID? 번호를 저장 해둠
next_board =  [ [ [] for _ in range(N) ] for _ in range(N) ]
new_board = [ [ [] for _ in range(N) ] for _ in range(N) ]
smell_board = [ [0 for _ in range(N)] for _ in range(N)]
smell_id_board = [ [-1 for _ in range(N)] for _ in range(N)]
# 상어 : [등수 번호, x, y, 방향(0123)] shark

# 1. 현재 상어의 위치에 냄새 K를 저장함
# 2. 그리고, 냄새 ID 보드에 ID를 저장함

for s in shark:
    # print("상어 초기화 : ",s)
    smell_board[s[1]][s[2]] = K
    smell_id_board[s[1]][s[2]] = s[0]

# print(*smell_board, sep='\n')
# print(*smell_id_board, sep='\n')

while True :
    # 종료 조건
    if total_count == 1 :
        print(times)
        break

    # print(times, total_count)
    # 새로운 shark 대입!
    # if times >= 1 :
    #     shark = []
    #     print("#####", *next_board, "####", sep='\n')
    #     for i in range(N) :
    #         for j in range(N) :
    #             if next_board[i][j] :
    #                 shark.append(*next_board[i][j])
    #     # 넥스트 보드 초기화
    #     next_board = [[[] for _ in range(N)] for _ in range(N)]

    # 모든 상어에 대해
    # 3. 다음 상어 위치를 결정함 각 상어에 대해 dx dy 를 진행하는데
    # 3-1. 4방향 검사, 냄새가 없다면(0)이라면 그 자리로 이동 -> break (nextboard에 shark append)
    # 3-2. 4방향 모두 검사했을 때, 냄새가 다 있다면, 냄새 ID로 4방 검사
    # 3-3. 나랑 같은게 있다면 그쪽으로 이동 후, 냄새 K로 갱신
    # print("새로운상오어어어", shark)
    for s in shark :
        # delta = s[0] ..
        # s[0] .. check_dir[s[0]] --> [[1, 2, 0, 3], [3, 0, 1, 2], [2, 3, 1, 0], [3, 2, 0, 1]]
        # check_dir[s[0]][s[3]] [1, 2, 0 3]
        # 얘를 기반으로 for i in range(4) : 대신에 foreach
        # print(check_dir[s[0]][s[3]])
        # print(s)
        flag = False
        for d in check_dir[s[0]][s[3]] :
            nx = s[1] + dx[d]
            ny = s[2] + dy[d]

            # 경계 안에 있어야 하고
            if 0 > nx or 0 > ny or nx >= N or ny >= N : continue

            if smell_board[nx][ny] == 0 :
                s[1], s[2] = nx, ny
                s[3] = d # 방향도 바꿔줌
                next_board[nx][ny].append(s)
                flag = True
                break

        if flag : continue
        for d in check_dir[s[0]][s[3]]:
            nx = s[1] + dx[d]
            ny = s[2] + dy[d]

            # 경계 안에 있어야 하고
            if 0 > nx or 0 > ny or nx >= N or ny >= N: continue

            if smell_id_board[nx][ny] == s[0]:
                s[1], s[2] = nx, ny
                s[3] = d  # 방향도 바꿔줌
                next_board[nx][ny].append(s)
                break

    # 3-3-1. 상어의 냄새보드에서 냄새를 -1씩 함
    # 3-3-2. 냄새보드를 다 체크해서 0이면 냄새 ID 보드에도 다 0으로 처리
    for i in range(N) :
        for j in range(N) :
            if smell_board[i][j] > 0 :
                smell_board[i][j] += -1
            if smell_board[i][j] == 0 :
                smell_id_board[i][j] = -1

    # 3-4. NEXT board 를 모두 점검 했을 때 len >= 2 이상이면
    # 그 칸에 대해서 sort key=lambda x : x[0] 오름차순 정렬
    # 그칸 = 그칸[0] 으로 나머지를 다 제거해줌
    # print(*next_board, sep='\n')

    for i in range(N) :
        for j in range(N) :

            if len(next_board[i][j]) >= 2 :
                # print(next_board[i][j])
                # print(*next_board,sep='\n')
                next_board[i][j].sort(key = lambda x : x[0])
                # print("삭제 전 ", next_board[i][j])
                total_count = total_count - (len(next_board[i][j]) - 1)
                remain_temp = next_board[i][j][0]
                next_board[i][j] = []
                next_board[i][j].append(remain_temp)
                # next_board[i][j] = next_board[i][j][0]


                # print("삭제 후 ", *next_board, sep='\n')

            if next_board[i][j] :  # 뭔가 있으면
                smell_board[i][j] = K
                smell_id_board[i][j] = next_board[i][j][0][0]

    # print("냄새 ID 보드")
    # print(*smell_id_board, sep='\n')
    # # 기존 보드로 복사
    # # for i in range(N) :
    # #     for j in range(N) :
    # #         if next_board[i][j] :
    # #             board[i][j] = next_board[i][j]
    # print("삭제 체크 이후 ")
    # print(*next_board, sep='\n')
    shark = []

    for i in range(N):
        for j in range(N):
            if next_board[i][j]:
                shark.append(*next_board[i][j])
    # 넥스트 보드 초기화
    next_board = [[[] for _ in range(N)] for _ in range(N)]

    times += 1
    if times > 1000 :
        # print(total_count)
        print(-1)
        # print(*next_board, sep='\n')
        break
    # 6. 새로운 냄새를 기록함.