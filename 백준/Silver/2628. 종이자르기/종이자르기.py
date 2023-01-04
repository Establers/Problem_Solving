x, y = map(int,input().split())
cnt = int(input())
x_list = [0, x]
y_list = [0, y]
# cutting = []
for i in range(cnt) :
    ver, length = (map(int, input().split()))
    if ver == 0 : # 가로
        y_list.append(length)
    else :
        x_list.append(length)

x_list.sort()
y_list.sort()

result = 0
# print(y_list)
for i in range(len(x_list)-1) :
    for j in range(len(y_list)-1) :
        w = x_list[i+1] - x_list[i]
        h = y_list[j+1] - y_list[j]
        result = max(result, w*h)

print(result)
