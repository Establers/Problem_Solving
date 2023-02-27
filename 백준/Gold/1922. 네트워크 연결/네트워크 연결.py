# 네트워크 연결

import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        p = find_parent(parent, parent[x])
        parent[x] = p
    return parent[x]

def union_parent(parent, a, b) :
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    if a_root < b_root :
        parent[b_root] = a_root
    else :
        parent[a_root] = b_root

N = int(input())
M = int(input())

edges = []
parent = [ i for i in range(N+1)]

for _ in range(M) :
    a, b, cost = map(int, input().split())
    edges.append( (a, b, cost) )

edges.sort(key = lambda x : x[2])

answer = 0
for edge in edges :
    a, b, cost = edge

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        answer += cost

print(answer)