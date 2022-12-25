import sys

x = sys.stdin.readline().rstrip()

for i in x : 
    if i.isupper() == 1 : 
       print(i.lower(),end='')
    else : print(i.upper(), end='')
