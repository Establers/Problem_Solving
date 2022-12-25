import sys

T = int(sys.stdin.readline())

while True :
    try : 
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except : break