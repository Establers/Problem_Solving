import sys

n = int(sys.stdin.readline())
num = 666
# 어쨌든 666 보다 클 것이기에.. 666에서 1씩 증가시켜 확인
cnt = 0

while n :  # n번째 동안 
    if '666' in str(num) : # 특정 num 에 666이 포함될 경우 
        n = n-1   # 다음 경우 찾기
    num = num + 1 # 반복적인 1 증가 
    # 1씩 증가시킨다면 어차피 크기 순으로 확인하는 것임.

print(num-1)  # 1증가하고 끝나기에 -1 다시