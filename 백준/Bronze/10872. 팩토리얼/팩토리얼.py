import sys

x = int( sys.stdin.readline().rstrip())
ans : int  = 1

if (x == 0) : 
    print("1")
else :       
    for x in range(1,x+1) : 
        ans =  ans * x
    print (ans)
