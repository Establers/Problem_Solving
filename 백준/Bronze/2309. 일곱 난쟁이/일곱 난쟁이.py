# 9명 중 7명 합이 100이 됨

list_h = []
for _ in range(9) :
    list_h.append(int(input()))
# print(list_h)
# 9명중 7명 선택 후 키 sum
all_sum = sum(list_h)

for i in range(0,8) :
    if sum == 100 : break
    for j in range(i+1, 9) :
        a = list_h[i]
        b = list_h[j]
        sum = all_sum - a - b
        # print(sum)
        if sum == 100 :
            list_h.remove(a)
            list_h.remove(b)
            list_h.sort()
            print(*list_h, sep='\n')
            break
        else :
            continue