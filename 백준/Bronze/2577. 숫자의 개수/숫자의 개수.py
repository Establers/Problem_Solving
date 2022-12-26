import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

for i in range(0,9+1) : 
    cnt = str(a*b*c).count(str(i))
    print(cnt)
