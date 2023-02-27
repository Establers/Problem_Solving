# 집합의 표현
# 1717 골드 5
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_parent(parent : list, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent , a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split())

edges = []
# parent = [0] * (v+1)
parent = [ i for i in range(0, v+1)]

for _ in range(e) :
    type, a, b = map(int, input().split())
    if type == 0 :
        union_parent(parent, a, b)

    elif type == 1 :
        c_a = find_parent(parent, a)
        c_b = find_parent(parent, b)
        if c_a == c_b :
            # 서로 같은 집합에 포함되어 있음
            print("YES")
        else :
            print("NO")