"""
list : 각 구역?에 해당하는 걸리는 시간
# 1. target : 우리가 구하고자 하는 특정 시간
# 2. 0초와 이산적으로 계산할 수 있는 최대로 걸리는 시간인 max(list) * m
# 3. 위 둘을 left , right로 두어 mid 값을 구한다.
# 4. mid 값을 기준으로 이 mid sec가 지났을 때 몇명을 체크할 수 있는지
# 각 노드별 검사 인원 수를 구한다.
# 5. 검사 인원 수인 m과 비교해 l, r 을 조정한다. m보다 크다면 정답을 갱신한다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
list = []
for _ in range(n) :
    list.append(int(input()))
# 1. target : 우리가 구하고자 하는 특정 시간

# 2. 0초와 이산적으로 계산할 수 있는 최대로 걸리는 시간인 max(list) * m
left = 0
right = max(list) * m
# 3. 위 둘을 left , right로 두어 mid 값을 구한다.
answer = right

def lower_bound() :
    global left, right, answer

    while left <= right :
        mid_time = (left + right) // 2
        checked = 0

        # 4. mid 값을 기준으로 이 mid sec가 지났을 때 몇명을 체크할 수 있는지
        # 각 노드별 검사 인원 수를 구한다.
        for i in range(n) :
            checked += mid_time // list[i]

        # 5. 검사 인원 수인 m과 비교해 l, r 을 조정한다. m보다 크다면 정답을 갱신한다.
        if checked >= m :
            answer = min(answer, mid_time)
            # mid_time이 크니까 줄여야한다.
            right = mid_time - 1

        else :
            # mid_time을 늘려야한다.
            left = mid_time + 1

lower_bound()
print(answer)