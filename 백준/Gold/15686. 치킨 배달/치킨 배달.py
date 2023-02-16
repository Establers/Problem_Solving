import sys
input = sys.stdin.readline

board = []
chicken_x_y = []
house_x_y = []
answer = int(1e9)
N, M = map(int, input().split())

for i in range(N) :
    board.append(list(map(int, input().split())))

for i in range(N) :
    for j in range(N) :
        if (board[i][j] == 2) :
            chicken_x_y.append((i,j))
        elif (board[i][j] == 1) :
            house_x_y.append((i,j))
#print(house_x_y)
import itertools


def find_distance(x,y, a,b) :
    return abs(x-a) + abs(y-b)

def backtracking():
    pass
    # 치킨집 여러개 중에 M개를 선택해야함

for chick in itertools.combinations(chicken_x_y, M) :
    result = 0
    #print("지금 치킨집 : ", chick)

    for x,y in house_x_y :
        min_distance = int(1e9)
        for a,b in chick :
            min_distance = min(min_distance,find_distance(a,b,x,y))

        result += min_distance

    answer = min(answer, result)


    # for a,b, in chick :
    #     for x,y in house_x_y :
    #         result += find_distance(a,b,x,y)
    #         print(result)
    # answer = min(result, answer)

print(answer)