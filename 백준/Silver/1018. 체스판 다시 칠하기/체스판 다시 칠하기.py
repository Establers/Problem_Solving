import sys
input = sys.stdin.readline

x, y = map(int,input().split()) # Test case 

pattern_WB = ["WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW","WBWBWBWB", "BWBWBWBW"]
pattern_BW = ["BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"]

board = []
for _ in range(x) : 
    board.append(input())

flag = 0
ans = 0

for idx_x in range(x-7) :
    for idx_y in range(y-7) :   # 8x8 접근 
        count = 0
        for i in range(8) : 
            for j in range(8) :  # 8x8 슬라이싱
                if board[idx_x+i][idx_y+j] != pattern_WB[i][j] :  # 패턴WB와 비교 다르면 하나씩 증가
                    count += 1  # 다른게 있을 때 마다 값을 누적해서 증가시킴 
        if (flag == 1) : 
            ans = min(ans, count)  # 8x8 비교가 끝나면 기존 값과 비교해서 작은 값을 넣기
        else : # 처음에는 그냥 값넣기
            flag = 1
            ans = count
        count = 0  # WB와 비교해봤으니 BW와도 비교해보기..
        for i in range(8) : 
            for j in range(8) :
                if board[idx_x+i][idx_y+j] != pattern_BW[i][j] :  # 패턴BW와 비교 다르면 하나씩 증
                    count += 1
        ans = min(ans, count)
print(ans)
