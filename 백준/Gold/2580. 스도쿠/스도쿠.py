import sys
input = sys.stdin.readline

mat = []
for i in range(9) :
    li = list(map(int, input().split()))
    mat.append(li)

# 9x9 visited 생성
visited1 = [[False] * 9 for _ in range(9)]
# 가로 확인

visited2 = [[False] * 9 for _ in range(9)]
# 세로 확인

visited3 = [[False] * 9 for _ in range(9)]
# 3x3 박스 확인
# 012
# 345
# 678

for i in range(9) :
    for j in range(9) :
        if mat[i][j] != 0 :
            visited1[i][mat[i][j]-1] = True # mat 1~9 -> 0~8
            visited2[j][mat[i][j]-1] = True
            visited3[i//3 * 3 + j//3][mat[i][j]-1] = True


# 0 0 > 0 8
# 1 0 > 1 8
def bt(x, y) :
    # end
    if(x == 9) : # 경계 밖
        return True

    # 숫자가 0이 아니면 다른 곳으로 bt 생성 후 return # 쭉 퍼져나가야해서
    if(mat[x][y] != 0) :
        ny = y + 1
        nx = x
        if (ny >= 9):
            ny = 0
            nx = x + 1

        return bt(nx, ny)
    else :
        for num in range(0, 9) :
            # 숫자 넣기 전
            # 각 visited 점검 후 모두 False 면 숫자 넣고 bt
            if (visited1[x][num] or visited2[y][num]
                or visited3[x//3 * 3 + y//3][num]) :
                continue

            mat[x][y] = num+1
            # visit 처리
            visited1[x][num] = True
            visited2[y][num] = True
            visited3[x//3*3 + y//3][num] = True

            ny = y + 1
            nx = x
            if(ny >= 9) :
                ny = 0
                nx = x + 1
            if(bt(nx, ny) == True) :
                return True
            # y가 9를 넘으면 리스트 인덱스를 넘어서
            # 9가 넘으면 1씩 더해주고, y좌표 쪽은 1씩 증가시키지만
            # 9를 넘지 않게 하기위해서 연산으로 0~8만 나오게 함 (1씩은 증가시키면서)
            mat[x][y] = 0
            visited1[x][num] = False
            visited2[y][num] = False
            visited3[x//3 * 3 + y//3][num] = False
            # 실패했다면 원래대로 되돌리기
    return False

bt(0,0)
for i in mat:
    print(*i)