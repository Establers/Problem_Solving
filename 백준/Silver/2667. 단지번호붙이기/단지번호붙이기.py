import sys
input = sys.stdin.readline

n = int(input())
graph = []

for i in range(n) :
    graph.append(list(map(int, input().rstrip())))
    # split 안해야 1, 0, 1,.. 이런식으로 들어감

def dfs(x, y) :
    global result
    global count
    if (0 <= x < n and 0 <= y < n) != True :
        return False

    if (graph[x][y] == 1) :
        graph[x][y] = 0
        count += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

result = 0
count = 0
num_house = []

for i in range(n) :
    for j in range(n) :
        if dfs(i,j) == True :
            result += 1
            num_house.append(count)
            count = 0

print(result)
num_house.sort()
print(*num_house, sep='\n')