import sys
input = sys.stdin.readline

list_ = []

n = int(input())

for i in range(n) :
    list_.append(int(input()))

#1 산술평균
sum_list = sum(list_)
print(int(round(sum_list / len(list_),0)))

#2 중앙값
list_.sort()
print(list_[int(n/2)])

#3 최빈값
cnt = 0
max_cnt = 1
value = 0
cnt_list = []
last_value = list_[0]

for i in list_ :
    value = i
    if value == last_value :
        cnt += 1
    else : # 값이 달라지면
        # 누적된 cnt 값이 기존 맥스카운트보다 크면
        if (cnt > max_cnt) :
            cnt_list = [] # 이전 값 다 제거
            max_cnt = cnt # 최대 값 갱신
            cnt_list.append(last_value) # 숫자를 추가
        elif (cnt == max_cnt) :
            cnt_list.append(last_value) #

        cnt = 1
    last_value = value

if (cnt > max_cnt):
    cnt_list = []  # 이전 값 다 제거
    max_cnt = cnt  # 최대 값 갱신
    cnt_list.append(last_value)  # 숫자를 추가
    last_value = value

elif (cnt == max_cnt):
    cnt_list.append(last_value)  #
    last_value = value

# print(cnt_list)
if len(cnt_list) >= 2 :
    print(cnt_list[1])
else :
    print(cnt_list[0])



#4 범위
print(abs(max(list_) - min(list_)))


