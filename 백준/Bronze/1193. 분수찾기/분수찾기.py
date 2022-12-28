import sys

n = int(sys.stdin.readline())

"""
/ /  /
/  /
/
지그재그의 한 패턴당 숫자가 포함되는 것이 규칙적이다라는 것을
확인할 수 있음

"""

zig = 1 # 첫번째 라인부터
while (n > zig) :   # n이 몇번째 대각선에 있는지 확인
    n = n - zig
    zig += 1
    # print(n)

if (zig % 2 == 0) : 
    print("{0}/{1}". format(n, zig+1-n))
else : 
    print("{1}/{0}". format(n, zig+1-n))


