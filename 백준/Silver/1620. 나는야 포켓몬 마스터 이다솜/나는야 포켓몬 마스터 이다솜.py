import sys
input = sys.stdin.readline

N, M = map(int , input().split())
pica = dict()

for i in range(1,N+1) :
    a = input().rstrip()
    pica[i] = a
    pica[a] = i

for i in range(M) :
    pb = input().rstrip()
    if str(pb).isdigit() == True :
        print(pica.get(int(pb)))
    else :
        print(pica.get(pb))