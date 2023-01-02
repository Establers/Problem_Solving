square = [[0 for _ in range(100)] for _ in range(100)]
# print(square)
result = 0
def zeroToOne(x,y,a,b) :
    for i in range(x, a) :
        for j in range(y, b) :
            square[i][j] = 1

for _ in range(4) : # 4번 입력받음
    x, y, a, b = map(int, input().split())
    zeroToOne(x,y,a,b)

for a in range(len(square)) :
    for b in range(len(square)) :
        if square[a][b] > 0 :
            result += 1

print(result)