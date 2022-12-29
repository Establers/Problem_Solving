import sys
input = sys.stdin.readline

T = int(input())
list_all = []

for tc in range(T) :
    _list = list(map(int, input().split()))
    # [55, 185]
    list_all.append(_list)
    #[ [55, 185], ... ]

# 덩치 입력 완료

for i in range(T) : 
    cnt = 1
    for j in range(T) :
        if list_all[i][0] < list_all[j][0] and list_all[i][1] < list_all[j][1] :
            cnt += 1
    print(cnt, end=' ')

