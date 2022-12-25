import sys

N, M = map(int, sys.stdin.readline().split())

list_a = [[0 for j in range(M) ] for i in range(N) ]
list_b = [[0 for j in range(M) ] for i in range(N) ]
# N M 행렬 생성

for A in range(N) : 
    list_a[A] = list(map(int, sys.stdin.readline().split()))

for B in range(N) : 
    list_b[B] = list(map(int,sys.stdin.readline().split()))

for x in range(N) :
    for y in range(M) :
        list_a[x][y] = list_a[x][y] + list_b[x][y]

for row in list_a :
    print(*row)

