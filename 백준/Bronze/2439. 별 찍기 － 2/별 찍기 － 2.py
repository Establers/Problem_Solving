import sys

line = int(sys.stdin.readline())
# line = 5
# for i in range(line) :
#     for _ in range(line-i-1) :
#         print("ㅁ", end='')
#     print((i+1) * "ㅋ",end='\n')
for i in range(line) :
    print((line-i-1) * " ", end='')
    print((i+1) * "*",end='\n')