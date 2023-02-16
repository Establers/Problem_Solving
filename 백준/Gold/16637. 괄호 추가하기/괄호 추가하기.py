from collections import deque
# stack?
# a 연산자 b 형태 만 가능


# def dfs(idx, result) :
#     global answer
#     global number_stack
#     # 0 1 2 3
#     if idx >= n // 2:  # 끝까지 온다는 것
#         # 계산 후 return
#         print("여긴오니?")
#         print(result)
#         answer = max(answer, result)
#         return
#
#     print("now : ", idx)
#     if idx + 1 < n // 2:
#         dfs(idx + 1, cal(result, number_stack[idx + 2], calcu_stack[idx + 1]))
#
#     if idx + 2 < n // 2:  # 4
#         # dfs(idx+2, cal(result, number_stack[idx+3],calcu_stack[idx+2]))
#         # 옆에꺼 계산?
#         dfs(idx + 2, cal(result
#                          , cal(number_stack[idx + 3], number_stack[idx + 2], calcu_stack[idx + 2])
#                          , calcu_stack[idx + 1]
#                          )
#             )
#     global calcu_stack

def dfs2(idx, result) :
    global answer
    global calcu_stack
    global number_stack
    # 3 + 8 * 7 - 9 * 2
    # 0 1 2 3 4 5 6 7 8
    if idx >= n-1 : # 끝까지 온다는 것
        # 계산 후 return
        # print("여긴오니?")
        # print(result)
        answer = max(answer, result)
        return
    # idx 짝수임
    # print("now : ", idx)
    if idx + 2 < n :
        dfs2(idx+2, cal(result, int(all_stack[idx+2]), all_stack[idx+1]))

    if idx + 4 < n : # 4
        # 괄호 선 계산

        dfs2(idx+4, cal(result
                        , cal(int(all_stack[idx+2]), int(all_stack[idx+4]), all_stack[idx+3])
                        , all_stack[idx+1]))

def cal(num1, num2, cal) :
    #print("{} {} {}".format(num1, cal, num2))
    if (cal == '+') :
        return num1 + num2
    elif (cal == '-') :
        return num1 - num2
    elif (cal == '*') :
        return num1 * num2


n = int(input())
temp = input()

number_stack = []
calcu_stack = []
all_stack = []
for i in temp :
    all_stack.append(i)
    # if i.isdigit() :
    #     number_stack.append(int(i))
    # else :
    #     calcu_stack.append(i)

answer = -2**31 + 1
dfs2(0, int(all_stack[0]))
print(answer)




"""
3 8 7 9 2
0 1 2 3 4   idx

0을 선택시 0,1 -> 2부터 선택해야함

ㅂㅌㄹㅋ이 아닌데

하나하나씩 모두 검사하면
3 8 7 9 2 다 따로
3 8 7 92    기호 idx 3
3 87 9 2 기호 idx 1
3 87 92 기호 idx  1 3
38 7 9 2
38 79 2
38 7 92
계산할 때 마다 최대 값 갱신
"""
# 3+8*7-9*2
# 인덱스를 + x - x 가 있으면
#        0 1 2 3
# + 을 선택 했을땐 -나 *
# * 을 선택 했을땐 *
# 즉 기호 양옆 인덱스는 선택 못하..ㅁ
