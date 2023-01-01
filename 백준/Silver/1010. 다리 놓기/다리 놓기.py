import sys
input = sys.stdin.readline

T = int(input()) # Test case 
"""
McombN 6개가 4개선택 M6 N4 일때 ..ㅇ
"""
def facto(a) : 
    val = 1
    for i in range(1, a+1) :
        val = val*i
    return val

def combination(a,b) :
    # a! / ((a-b)!*b!)
    return int(facto(a) / (facto(a-b)*facto(b)))
    

for _ in range(T) : 
    a, b = map(int, input().split())
    print(combination(b,a))   
    # 받는건 N M 이지만 
    # M combination N 임