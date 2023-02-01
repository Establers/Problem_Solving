import sys
input = sys.stdin.readline

n, m = map(int ,input().split())
result = []
li = [0] * (m+1)
def backTracking(depth, li : list, i) :
    if(promising(depth, i, li)== True) :
        if (depth == m) :# end 조건
            #result.append(li[1:])
            print(*li[1:])
        else :
            for i in range(1, n+1) :
                li[depth+1] = i
                backTracking(depth+1, li, i)


def promising(depth, i, li : list) :
    if (li[depth-1] <= i) :
        return True
    else : return False

backTracking(0,li,0)
