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

    for i in range(4) :
        if (math_list[i] > 0):
            if (i == 0):
                math_list[i] += -1
                temp = cal + number_list[depth + 1]
                dfs(i, temp, depth + 1)
                math_list[i] += 1
            elif (i == 1):
                math_list[i] += -1
                temp = cal - number_list[depth + 1]
                dfs(i, temp, depth + 1)
                math_list[i] += 1
            elif (i == 2):
                math_list[i] += -1
                temp = cal * number_list[depth + 1]
                dfs(i, temp, depth + 1)
                math_list[i] += 1
            elif (i == 3):
                math_list[i] += -1
                temp = (int)(cal / number_list[depth + 1])
                dfs(i, temp, depth + 1)
                math_list[i] += 1



n = int(input())
number_list = list(map(int, input().split()))
math_list = list(map(int, input().split()))
result_min = int(1e9)
result_max = int(-1e9)

for i in range(4):
    dfs(i, number_list[0], 0)

print(result_max, result_min, sep='\n')



