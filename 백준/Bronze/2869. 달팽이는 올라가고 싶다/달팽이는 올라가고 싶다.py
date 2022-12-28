import sys
import math
input = sys.stdin.readline

a, b, v = map(int,input().split())

# 1일에 a - b 만큼 올라감
# 5 3 6 -> 하루에 2만큼 올라감 근데
# 6 / (5-3) 하면 3인데 올라갈 때 정상을 찍는 순간 끝이 나기때문에
# 막대 높이에서 내려가는 길이를 빼면 실질적으로 올라가는 거리
# 계산식은 (v-b) / (a-b) 가 됨 
# 소수니 올림필요

print(math.ceil((v-b)/(a-b)))
