import sys
input = sys.stdin.readline
from collections import deque


t = int(input())


li_1 = deque()
li_2 = deque()
for tc in range(t) :
    command = list(input().rstrip())
    for i in command :
        if (i == '<') :
            if(li_1) :
                li_2.appendleft(li_1.pop())
        elif (i == '>') :
            if(li_2) :
                li_1.append(li_2.popleft())
        elif (i == '-') :
            if(li_1) :
                li_1.pop()
        else :
            # 문자를 커서 위치에 추가
            li_1.append(i)

    print(*li_1, *li_2, sep='')
    li_1.clear()
    li_2.clear()


