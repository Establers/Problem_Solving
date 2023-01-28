import sys
input = sys.stdin.readline

n = int(input())
graph = [] #

for i in range(n) :
    a, b = map(int , input().split())
    graph.append((a,b))
    # a <= b 인건 명백한가?... 과거에 끝나는 회의는 없다고 생각..

graph.sort(key = lambda x : (x[1], x[0]))

# print(graph)

count = 0
lastTime = 0

for a, b in graph :
    if a >= lastTime :
        count += 1
        lastTime = b

print(count)