import sys

a = int( sys.stdin.readline().rstrip())

if 90 <= a:
    print("A")
elif 80 <= a :
    print("B")
elif 70 <= a :
    print("C")
elif 60 <= a :
    print("D")
else : print("F")