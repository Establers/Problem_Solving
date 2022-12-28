import sys

input = sys.stdin.readline
# test case
T  = int(input())

y_cnt = 0
k_cnt = 0

for _ in range(T) : # Test case 반복
    for _ in range(9) : 
        y, k = map(int, input().split())
        y_cnt += y
        k_cnt += k
    if (y_cnt == k_cnt) : 
        print("Draw")
    elif (y_cnt > k_cnt) : 
        print("Yonsei")
    else : print("Korea")
    y_cnt = 0
    k_cnt = 0

    
    
