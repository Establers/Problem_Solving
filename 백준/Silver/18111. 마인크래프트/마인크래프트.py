import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
# 3 4
mc_map = []
time = 0
result_time = 1e9
height = 0
for i in range(n) :
    mc_map.append(list(map(int, input().split())))
# print(mc_map)

for i in range(257) :
    add_block = 0
    sub_block = 0
    for x in range(n) : # 3
        for y in range(m) : # 4
            if mc_map[x][y] > i :
                sub_block += mc_map[x][y] - i
            else :
                add_block += i - mc_map[x][y]

    if add_block > sub_block + b :
        continue

    time = sub_block * 2 + add_block

    if time <= result_time :
        result_time = time
        height = i

print(result_time, height)



# for i in range(n) :


