n = int(input())
numList = list(map(int , input().split()))
numList.sort()

for i in range(1, n) :
    numList[i] = numList[i] + numList[i-1]

print(sum(numList))