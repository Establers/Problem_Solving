import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

p = 0
q = 0

for i in li :
    if i == 0 :
        q += 1
    elif i % 2 == 0 :
        p += -1
        q += -1
    else :
        p += 1
        q += -1

print(p,".000000000 ", q,".000000000", sep='')