import sys
input = sys.stdin.readline

n = int(input())
# black paper 10x10
white_paper = [[0 for i in range(100)] for j in range(100)]
count = 0
for i in range(n) :
    a, b = map(int, input().split())

    for i in range(10) :
        for j in range(10) :
            white_paper[a+i][99-j-b] = 1

for i in range(100) :
    for j in range(100) :
        if white_paper[i][j] == 1 :
            count += 1

print(count)
