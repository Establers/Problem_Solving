import sys

input = sys.stdin.readline


def find_parent(parent: list, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, weight = map(int, input().split())
    edges.append((weight, a, b))

edges.sort()

for edge in edges:
    weight, a, b = edge
    if (find_parent(parent, a) != find_parent(parent, b)):
        union_parent(parent, a, b)
        result += weight

print(result)