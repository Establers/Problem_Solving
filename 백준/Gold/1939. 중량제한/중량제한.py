import sys
input =sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

N, M = map(int, input().split())
edges = []
result = 0
parent = [ i for i in range(0, N+1)]

for _ in range(M) :
    a, b, weight = map(int, input().split())
    edges.append( (weight, a, b))

edges.sort(reverse=True)
# 내림차순으로 정렬
# print(edges)
start, end = map(int, input().split())

for edge in edges :
    weight, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)

    if find_parent(parent, start) == find_parent(parent, end) :
        # 두 부모가 같으면
        result = weight
        break
        # 합이나 총 거리를 구하는 그런 것이 아니라
        # 연결이 되는 순간의 weight 를 구하면 되는데
        # weight 의 최대값을 구하는 것이라
        # weight 순으로 내림차순을 정렬 해놓고
        # start , end의 부모를 체크하였다
        # 부모가 같다는 것은 그 순간 연결이 된 것이고
        # 그 때의 weight가 연결되는 간선 중 가장 큰 weight 일 것이다
        # 왜냐하면 weight 순으로 내림차순 정렬을 했기 때문이다
        # 간선 중에 weight가 높은게 있어도, 그 weight 중에서의 가장 작은 값을
        # 고르는 문제이다.

print(result)