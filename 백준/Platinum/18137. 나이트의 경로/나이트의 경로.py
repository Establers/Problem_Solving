import sys
input = sys.stdin.readline
import heapq

def mapper(x, y) :
    return (x + y - 1) * (x + y - 2) // 2 + y # 1,1 -> 1
    # 양의 정수에 대응

# knight
moves = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [-1, 2],
    [1, -2],
    [-1, -2],
]

def in_range(x, y) :
    return x > 0 and y > 0

visited = set()

k = int(input())

q = []
heapq.heapify(q)
visited.add((1, 1))
start = mapper(1, 1)
heapq.heappush(q, (start, (1,1)))
answer = start

for i in range(k+1) :
    if not q : break

    loc, (x, y) = heapq.heappop(q) # 제일 작은거 뽑기
    visited.add((x,y))
    answer = mapper(x, y)

    # print( "횟수 ",i,": ", x, y, "맵퍼 : ", mapper(x,y))

    sub_moveable = []
    for d in moves :
        nx = x + d[0]
        ny = y + d[1]

        if (nx, ny) not in visited and in_range(nx, ny):
            loc = mapper(nx, ny)
            heapq.heappush(sub_moveable, (loc, (nx,ny)))


    if sub_moveable :
        next_go = heapq.heappop(sub_moveable)
        heapq.heappush(q, next_go)


print(answer)