import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
height = list(map(int, input().split()))
# [6, 9, 5, 7, 4] # 탑들의 높이는 서로 다 다를
idx = 0
stack = deque()

stack.append((height[0], 1))
print(0, end=' ')

for i in range(1,N) :
    if(height[i] > stack[-1][0]) : # 들어갈려는게 더 크면
        # print(stack)
        while(len(stack) != 0 and height[i] > stack[-1][0]) :
            stack.pop()
        if(stack) :
            print(stack[-1][1], end=' ')
        else : # 빈 스택
            print(0, end=' ')
        stack.append((height[i], i+1))


    else :
        # 높이가 더 작을 경우
        # 스택의 가장 위에꺼의 idx 출력
        print(stack[-1][1], end=' ')
        stack.append((height[i], i+1))
