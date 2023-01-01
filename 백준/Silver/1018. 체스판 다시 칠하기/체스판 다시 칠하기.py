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
            for j in range(8) :
                if board[idx_x+i][idx_y+j] != pattern_WB[i][j] : 
                    count += 1
        if (flag == 1) : 
            ans = min(ans, count)
        else : 
            flag = 1
            ans = count
        count = 0
        for i in range(8) : 
            for j in range(8) :
                if board[idx_x+i][idx_y+j] != pattern_BW[i][j] : 
                    count += 1
        ans = min(ans, count)
print(ans)