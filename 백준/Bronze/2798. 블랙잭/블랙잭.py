# 100 Comb 3   .. NC3
#
from itertools import combinations
n, m = map(int, input().split())
idx_list = [i for i in range(0,n)]
card_num = list(map(int, input().split()))
value = 0
result = 0
for i in combinations(card_num, 3) :
    value = sum(i)
    if value > m : continue
    if abs(value - m) <= abs(result - m) : # 차이가 더 작은 경우
        result = value

print(result)