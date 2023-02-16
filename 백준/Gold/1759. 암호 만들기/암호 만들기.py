moum = ["a", "e", "i", "o", "u"]

L, C = map(int, input().split())
str_list = list(input().split())
str_list.sort()

# print(str_list)

# a..b...c..d..e 증가하는 순서로 넣어야 하고
# 최소 한개의 모음이 포함되어야 한다
temp = []
visited = [ False for _ in range(C) ]
result_list = [ 0 for _ in range(L) ]

def backtracking(depth, flag, idx):
    global result_list
    if(depth == L):
        count = 0
        for i in result_list :
            if (i in moum) :
                count += 1
        if(count >= 1 and L-count >= 2) :
            print(*result_list, sep='')
        return

    else :
        for i in range(idx, C) :
            if(flag & 1<<i) != 0 : continue
            result_list[depth] = str_list[i]
            backtracking(depth + 1, flag | (1<<i), i+1)

backtracking(0,0,0)



