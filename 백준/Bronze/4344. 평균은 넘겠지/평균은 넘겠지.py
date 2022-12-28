import sys

input = sys.stdin.readline
# test case
C = int(input())
cnt = 0
for _ in range(C) : 
    list_ = list(map(int, input().split()))
    avg =  (sum(list_[1:]))/ (list_[0])   # 평균계산
    for n in list_[1:]: 
        if (n > avg) : 
            cnt += 1

    print("{0:2.3f}%".format((cnt*100 / list_[0])))
    cnt = 0

