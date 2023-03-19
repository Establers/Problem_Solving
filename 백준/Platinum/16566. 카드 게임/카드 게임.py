import sys
import bisect as bi
input = sys.stdin.readline

n, m, k = map(int , input().split())

blue_seq = list(map(int, input().split()))
red_seq =list(map(int, input().split()))
blue_seq.sort() # 이분 탐색을 위한 정렬

def find_parent(parent, a) :
    if parent[a] != a :
        temp = parent[a]
        parent[a] = find_parent(parent, temp)
    return parent[a]

def union_parent(parent, a, b) :
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b  :
        parent[root_b] = root_a
    else :
        parent[root_a] = root_b

parent = [ i for i in range(0, n+1) ]


for i in range(k) :
    now_value = red_seq[i]
    idx = bi.bisect_right(blue_seq, now_value)
    while True :
        if find_parent(parent, blue_seq[idx]) != find_parent(parent, 0) :
            union_parent(parent, blue_seq[idx], 0)
            print(blue_seq[idx])
            break

        else :
            idx += 1