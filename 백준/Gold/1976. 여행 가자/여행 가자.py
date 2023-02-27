import sys
input = sys.stdin.readline

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

v = int(input())
e = int(input())
edges = [ [] for _ in range(v+1)]
# print(edges)
parent = [ i for i in range(0, v+1)]
# print(parent)
for i in range(1, v+1): # 1 2 3
    seq = list(map(int, input().split()))
    for j in range(len(seq)) : # 0 1 2
        if seq[j] == 1 :
            # edges[i].append(j+1)
            union_parent(parent, i, j+1)

visit_seq = list(map(int, input().split()))

def solution() :
    my_p = find_parent(parent, visit_seq[0])
    for node in visit_seq :
        temp = find_parent(parent, node)
        if temp != my_p :
            print("NO")
            return

    print("YES")

solution()