import sys
input = sys.stdin.readline

while True : 
    n = (input().rstrip())
    if int(n) == 0 : 
        break
    reverse_n = n[::-1] # 문자열은 이렇게 뒤집을수있다
    if(reverse_n == n) : 
        print("yes")
    else : 
        print("no")
    