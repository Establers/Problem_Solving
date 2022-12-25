import sys

N = int(sys.stdin.readline().rstrip())
num = input()
sum = 0
for i in range(0, N) : 
    sum = sum + int(num[0+i])  # 문자열 인덱싱 차례로 한 이후, int 캐스팅 후 SUM

print(sum)