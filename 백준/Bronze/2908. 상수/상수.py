import sys

a, b = map(str, sys.stdin.readline().split())

if (int(a[::-1]) > int(b[::-1])) : 
    print (a[::-1])
else : print (b[::-1])