import sys
input = sys.stdin.readline

# swea 4008 과 똑같음
def dfs(math : int, cal, depth) :
    global n
    global result_max
    global result_min
    global math_list

    if(depth == n-1) :
        result_max = max(result_max, cal)
        result_min = min(result_min, cal)
        return


    if (math_list[0] > 0):
        math_list[0] += -1
        temp = cal + number_list[depth + 1]
        dfs(0, temp, depth + 1)
        math_list[0] += 1


    if (math_list[1] > 0):
        math_list[1] += -1
        temp = cal - number_list[depth + 1]
        dfs(1, temp, depth + 1)
        math_list[1] += 1


    if (math_list[2] > 0):
        math_list[2] += -1
        temp = cal * number_list[depth + 1]
        dfs(2, temp, depth + 1)
        math_list[2] += 1


    if (math_list[3] > 0):
        math_list[3] += -1
        temp = (int)(cal / number_list[depth + 1])
        dfs(3, temp, depth + 1)
        math_list[3] += 1



n = int(input())
number_list = list(map(int, input().split()))
math_list = list(map(int, input().split()))
result_min = int(1e9)
result_max = int(-1e9)

dfs(0, number_list[0], 0)

print(result_max, result_min, sep='\n')