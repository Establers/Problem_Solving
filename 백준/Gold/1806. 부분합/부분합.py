import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

pre_sum = [0]
temp = 0
for i in nums :
    temp += i
    pre_sum.append(temp)

#print(pre_sum)

start = 0
end = 0
INF = 1e9 + 100
result = INF

while(True) :
    val = pre_sum[end] - pre_sum[start]
    #print(val, result,start)
    if (val >= s) : # 조건 만족
        result = min(result, end-start)
        if (start < n) :
            start += 1 # 합을 더 작게
    else :
        if(end == n) : break
        # s 보다 크지도 않고.. val을 더이상 크게할수도 읎음
        if(end < n) :
            end += 1 # 합을 더 크게(val을 더크게)

if (result == INF) :
    print(0)
else :
    print(result)
