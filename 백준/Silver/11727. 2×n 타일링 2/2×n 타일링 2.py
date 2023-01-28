import sys
input = sys.stdin.readline

n = int(input())
d = [1] *(n+1)
#   [.... n ....]
#   [...n-1 ..][]
#   [..n-2 ..][ ]
#   [..n-2 ..][ㅡ]
#   [..n-2 ..][|] -> n-1[]와 겹침 -> 생략
#   d[n] = d[n-1] + 2*d[n-2] 임.
def solution() :
    if(n == 1) :
        return print(1)
    elif(n == 2) :
        return print(3)

    d[1] = 1
    d[2] = 3

    for i in range(3,n+1) :
        d[i] = d[i-1] + 2*(d[i-2])

    return print(d[n] % 10007)

solution()