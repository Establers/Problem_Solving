import math
import sys
input = sys.stdin.readline

n = int(input()) # 자연수 n

d = [ True for i in range(n+1)] # true 소수
map_ = [0 for i in range(n+1)]

d[0:1] = False, False

for i in range(2, int(math.sqrt(n))+1) :
    if d[i] == True :
        for j in range(i+i, n+1, i) :
            if d[j] == True :
                d[j] = False

sum_val = 0
pre_sum = [0]
for i in range(n+1) :
    if(d[i] == True) :
        sum_val += i
        pre_sum.append(sum_val)

#print(pre_sum)

# count = 0
# #print(count)
# start = 0
# right = 1
# #print(len(pre_sum)-1) # 13까지 값 있음
# while(True) :
#     value = pre_sum[right] - pre_sum[start]
#     #print(value, right, start)
#     if (start == len(pre_sum) - 2):
#         if ((pre_sum[right] - pre_sum[start]) == n) :
#             # print("됐나..")
#             count += 1
#         break
#     if value == n :
#         count += 1
#         right += 1
#     if(value < n) :
#         right += 1
#     elif(value > n) :
#         start += 1
#
# print(count)

def find_sum() :
    if n == 1 :
        return 0
    count = 0
    # print(count)
    start = 0
    right = 1
    while (True):
        value = pre_sum[right] - pre_sum[start]
        # print(value, right, start)
        if (start == len(pre_sum) - 2):
            if ((pre_sum[right] - pre_sum[start]) == n):
                # print("됐나..")
                count += 1
            break
        if value == n:
            count += 1
            right += 1
        if (value < n):
            right += 1
        elif (value > n):
            start += 1

    return count

print(find_sum())