from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

n = int(input())
result = []
count = 1
for i in range(n) :
    number = int(input()) # 4

    while count <= number : # 만족하는 숫자까지 Push
        queue.append(count)
        count += 1
        # print("+") # 바로 Print 하면 NO만을 출력할 수 가 없음
        result.append("+")

    if number == queue[-1] : # 스택의 마지막과 받은 값이 같다면 POP
        queue.pop() # 1 2 3
        result.append("-")

    else :
        result.append("NO")
        break

if "NO" in result :
    print("NO")
else :
    print(*result,sep='\n')



