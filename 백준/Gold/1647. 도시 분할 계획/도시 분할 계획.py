# 도시 분할 계획
import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        p = find_parent(parent,parent[x])
        parent[x] = p
    return parent[x]

def union_parent(parent, a, b) :
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    if a_root < b_root :
        parent[b_root] = a_root
    else :
        parent[a_root] = b_root

N, M = map(int, input().split())

edges = []
parent = [ i for i in range(0, N+1) ]

for _ in range(M) :
    a, b, fee = map(int, input().split())
    edges.append((a,b,fee))

edges.sort(key = lambda x : x[2])

# ㅋㄹㅅㅋ
result = 0

for e in edges :
    a, b, fee = e

    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += fee
        last_fee = fee

answer = result - last_fee
print(answer)