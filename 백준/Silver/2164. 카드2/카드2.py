from collections import deque
N = int(input())
queue = deque([i for i in range(1,N+1)]) # 1~N 까지의 리스트 생성한 뒤 queue 형식으로
while len(queue) > 1 : # 한개일 때 까지 계속 진행
    queue.popleft() # 맨왼쪽에꺼를 빼내고
    queue.append(queue.popleft()) # 다시 맨왼쪽에꺼를 맨 오른쪽에 추가

print(queue[0])