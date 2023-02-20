import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def square(n, num) : # 나머지 연산을 이용해서 천문학적으로 큰 숫자 정리
    if n == 1 :
        return num

    temp = square(n//2, num)

    if n % 2 == 0 :
        return (temp * temp) % c
    else :
        return (temp * temp * num) % c # 잃어버린 1 만큼

def square2(n, num) : # 기본적인 것
    if n == 1 :
        return num
    if n % 2 == 0 :
        return square2(n//2, num) * square2(n//2, num)
    else :
        return square2(n//2, num) * square2(n//2, num) * num # 잃어버린 1 만큼

print(square(b,a) % c)