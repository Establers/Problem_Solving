from collections import deque

t = int(input())

for i in range(t) :
    sw = 0
    queue = deque()
    strr = input()

    for j in strr :
        if j == '(' :
            queue.append(j)
        elif j == ')':
            if queue :
                queue.pop()
                # print(queue)
            else : # 큐가 비어있을 경우
                print("NO")
                sw = 1
                break # 테스트 케이스를 종료
    # 수행이 끝난 경우
    # queue 점검
    if sw == 0 :
        if queue : # 큐에 무언가 존재할 경우
            print("NO")
        else :
            print("YES")

