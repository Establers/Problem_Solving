import sys
input = sys.stdin.readline

t = int(input())

temp = [1]
value = 0
# 0층


for i in range(t) :
    floor_ = int(input())
    ho_ = int(input())
    zeroFloor = [[0 for _ in range(ho_)] for _ in range(floor_ + 1)]
    # print(zeroFloor)

    for a in range(0,ho_) :
        zeroFloor[0][a] = a+1

    for j in range(1, floor_+1) : #1이 2층
        for k in range(0, ho_) :
            if (k == 0) :
                zeroFloor[j][k] = 1
            else :
                zeroFloor[j][k] = zeroFloor[j-1][k] + zeroFloor[j][k-1]
    # print(zeroFloor)
    print(zeroFloor[floor_][ho_-1])
