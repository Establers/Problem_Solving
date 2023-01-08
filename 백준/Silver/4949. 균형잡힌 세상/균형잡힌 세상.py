import sys
input = sys.stdin.readline

while True :
    queue = []
    input_string = input().rstrip() # 한줄 입력 ?

    if (input_string == '.') :
        # print("yes")
        break

    for a in input_string :
        if a == '(' or a == '[' :
            queue.append(a)

        elif a == ')' :
            if queue and queue[-1] == '(' :
                queue.pop()
            else :
                queue.append(a)

        elif a == ']' :
            if queue and queue[-1] == '[' :
                queue.pop()
            else :
                queue.append(a)

    if len(queue) == 0 :
        print('yes')
    else :
        print('no')
