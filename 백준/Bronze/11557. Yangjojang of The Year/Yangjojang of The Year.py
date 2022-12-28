import sys

input = sys.stdin.readline
# test case
T  = int(input())
name = ' '
liter = 0

for _ in range(T) : # Test case 반복
    # 학교의 숫자
    N  = int(input())
    for _ in range(N) : # 술 받기
        name_, liter_ = sys.stdin.readline().split()
        if (int(liter_) > liter) : 
            liter = int(liter_)
            name = name_
    print(name) # 이 test case의 학교 이름 고치기