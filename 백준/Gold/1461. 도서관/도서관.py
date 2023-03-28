import sys
input = sys.stdin.readline

n,m = map(int, input().split())

a = list(map(int, input().split()))

u_c = []
l_c = []

for i in range(n) :
    if a[i] > 0 :
        u_c.append(a[i])
    else  :
        l_c.append(-a[i])

umx, lmx = 0, 0
if u_c != [] :
    u_c.sort()
    umx = u_c[-1]
if l_c != [] :
    l_c.sort()
    lmx = l_c[-1]

dt_max = max(umx,lmx)

# 오른쪽 끝에서 부터 선택 m개
result = 0
def select2(list) :
    global result
    for i in range(len(list)-1, -1, -m) :
        result += list[i] * 2

select2(u_c)
select2(l_c)
print(result - dt_max)