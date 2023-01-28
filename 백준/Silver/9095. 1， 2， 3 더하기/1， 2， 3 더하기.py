import sys
input = sys.stdin.readline

t = int(input())
# 1 : 1
# 2 : 2
# 3 : 4
# 4 : 7
# 5 : 13
# 6 : 24
"""
111 1
21 2
3 1

11111 1
2111 .. 4
221 3
32 2
311 3
5 : 13개

6 : 
111111 1
21111 5 
2211 6
222 1
3111 4
321 312 213 231 123 132 6
33 1 
: 17 7 = 24

각 베이스 경우의 수 계산,

"""
d = [0] * 11
d[1:3] = 1, 2, 4

for i in range(4,11) :
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in range(t) :
    # test case
    n = int(input())
    print(d[n])