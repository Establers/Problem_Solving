# 2231
# N + 각 자리수 합....
import sys
input = sys.stdin.readline

n = int(input())
def hap(num) :
    return sum(list(map(int, str(num)))) + num

for i in range(1, n+1) :
    result = hap(i)
    # print(result)
    if result == n :
        print(i)
        break
    if i == n :
        print(0)
