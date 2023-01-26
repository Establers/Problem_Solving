import sys
input = sys.stdin.readline

N, S = map(int, input().split())

list_ = list(map(int, input().split()))
# 수가 들어있는 리스트

pre_sum = [0]
sum_value = 0

# 연속된 수 이여서 구간 합.
for i in list_ :
    sum_value += i
    pre_sum.append(sum_value)

# print(pre_sum)
# 구간 합 완성
# [0, 5, 6, 9, 14, 24, 31, 35, 44, 46, 54]

# 구간 합을 뒤져가면서 S 넘고, 길이가 가장 짧은 것 찾기 min
# 구간 합 탐색
start = 0
end = 0
INF = 1e9
result = INF
while(True) :
    value = pre_sum[end] - pre_sum[start]
    #print(value,start, end)

    if (value >= S) :
        #print(value, start, end)
        result = min(result, end - start)
        # print("결과1 : ", result)
        start += 1
        #print(start)
    else : # 작다면
        if (end == len(pre_sum) - 1):
            break
        if (end < len(pre_sum) - 1):
            end += 1


if result != INF :
    print(result)
else :
    print(0)

#10 15
#1 1 1 1 1 1 1 1 1 2