import sys
input = sys.stdin.readline

n = int(input())
stairs = []
for i in range(n) :
    stairs.append(int(input()))

d = [0] * (n+1)

# 연속 세칸 X
# 1칸 or 2칸
# 바닥에서 시작
# 마지막 칸 무조건 밟
def find_score() :
    if(n == 1) : return stairs[0]
    
    d[0] = stairs[0]
    d[1] = stairs[1] + stairs[0]

    for i in range(2, n) :
        d[i] = max(stairs[i] + stairs[i-1] + d[i-3]
                   , stairs[i] + d[i-2])

    return(d[-2])

print(find_score())