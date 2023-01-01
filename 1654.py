####### 고쳐야함 #########

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
_list = [] 
for i in range(K) : 
    _list.append(int(input()))

min = min(_list)
length = 0
Flag = False

# i 길이 최소 값에서 시작 그래야 선을 다 자를 수 있으니
for i in range(min,0,-1) : 
    count = 0              # count 자를 수 있는 선의 총합
    # if Flag == True and length > i :
    #     break
    for j in _list :       # j 각 선들의 길이
        count += j // i    # 선을 잘라 나오는 개수
    if (count >= N) :      # 잘라서 나온게 N개 보다 많으면
        length = max(length, i) # 길이를 비교해 긴 것으로 갱신
        Flag = True

print(length) # 답을 구했지만 완전탐색이라 탈출이 필요할 듯
