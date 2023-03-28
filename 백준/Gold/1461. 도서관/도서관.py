import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a = list(map(int, input().split()))

upper_case = []
lower_case = []

for i in range(n) :
    if a[i] > 0 :
        upper_case.append(a[i])
    else  :
        lower_case.append(-a[i])

umx, lmx = 0, 0
if upper_case != [] :
    upper_case.sort()
    umx = upper_case[-1]
if lower_case != [] :
    lower_case.sort()
    lmx = lower_case[-1]

dt_max = max(umx,lmx)
# to be substract

# 오른쪽 끝에서 부터 선택 m개
result = 0
def select2(list) :
    global result
    for i in range(len(list)-1, -1, -m) :
        result += list[i] * 2

# select(upper_case)
# select(lower_case)

select2(upper_case)
select2(lower_case)
result -= dt_max
print(result)

"""
def select(list) :
    global result
    cnt = 0
    temp = []

    for i in range(len(list)-1, -1, -1) :
        cnt += 1
        temp.append(list[i])
        if cnt >= m :
            result += max(temp) * 2
            temp = []; cnt = 0;

    if temp != [] :
        result += max(temp) * 2
"""