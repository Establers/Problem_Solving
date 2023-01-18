# 하나를 구성하면 거기서 가장 큰 값을 제거하고 마을을 두개로 만든다 .
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

n, m = map(int, input().split())

edges = []
result = 0

parent = [0] * (n+1)
for i in range(1, n+1) :
    parent[i] = i

# parent = [ i for i in range(0, n+1)]
# [0 1 2 3 ... n] .. 집(노드)

for i in range(m) : # m만큼 값을 받는다 (간선에 대한 정보 입력)
    node1, node2, cost = map(int, input().split())
    edges.append( (cost, node1, node2) )
    # 비용 순으로 정렬하기 위해 edges에 추가를 한다.

edges.sort()
# 오름 차순으로 정렬해서 비용 순으로 되게한다.
max_val = 0

for edge in edges :
    cost, node1, node2 = edge
    # 비용 순으로 진행을 해 최소값을 찾도록 유도한다.
    if(find_parent(parent, node1) != find_parent(parent, node2)) :
    # 서로의 부모 노드가 다를 때 서로를 합해준다.
        union_parent(parent, node1, node2)
        result += cost
        # cost를 계속 누적해서 계산해준다
        max_val = cost
        # 도시를 두개로 나누기 위해서 나중에 간선하나의 cost를 빼줘야 하는데
        # 그거를 계산하기 위한 것 cost 순으로 정렬했기 때문에 마지막 것이 최대값이다.

print(result - max_val)
# 하나로된 도시를 두개로 나누기 위해
# 간선하나를 제거해줘야 하는데 비용이 가장 비싼 걸 제거해 두개로 나눈다.