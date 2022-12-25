import sys

x = int( sys.stdin.readline().rstrip())

if (x%4 ==0) : 
    if((x%100 != 0) or (x%400 == 0)) :
        print ("1")
    else : print("0")
else : print("0")