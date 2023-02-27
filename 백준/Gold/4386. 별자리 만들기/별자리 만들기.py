# 별자리 만들기
import math
import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        p = find_parent(parent, parent[x])
        parent[x] = p
    return parent[x]

def union_find(parent, a, b) :
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    if a_root < b_root :
        parent[b_root] = a_root
    else :
        parent[a_root] = b_root

def get_distance(x1, y1, x2, y2) :
    a = (x1 - x2)**2
    b = (y1 - y2)**2
    temp = math.sqrt(a+b)
    return temp

def get_distance2(a, b) :
    x = (a[0] - b[0])**2
    y = (a[1] - b[1])**2
    temp = math.sqrt(x+y)
    return temp



def bt(depth, arr : list, start) :
    if depth == 2 :
        # print(arr)
        # print(star_list)
        a = star_list[arr[0]]
        b = star_list[arr[1]]
        idx_a = star_list[arr[0]][2]
        idx_b = star_list[arr[1]][2]
        cost = get_distance2(a, b)
        # edges.append((cost, a, b))
        edges.append((cost, idx_a, idx_b))
        return

    for i in range(start, n) :
        if not visited[i] :
            visited[i] = True
            arr.append(i)

            bt(depth + 1, arr, i+1)
            visited[i] = False
            arr.pop()

n = int(input())
edges = []
parent = [ i for i in range(n+1) ]
visited = [False] * (n+1)

star_list = []

for i in range(1,n+1) :
    a, b = map(float, input().split())
    star_list.append((a,b,i))


# 두 별 사이만큼이 cost
bt(0, [], 0)

# print(edges)

edges.sort()
result = 0
for edge in edges :
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b) :
        union_find(parent, a, b)
        result += round(cost, 2)

if n != 1 :
    print(result)
else :
    print(0)