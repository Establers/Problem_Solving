import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find_parent(parent, x) :
    if parent[x] != x :
        p = find_parent(parent, parent[x])
        weight[x] += weight[parent[x]]  # 부모가 더 무게가 작은걸로 하고있음
        # 값을 더해주고 부모를 바꿔야함
        parent[x] = p
        # weight[x] += weight[parent[x]]  # 부모가 더 무게가 작은걸로 하고있음
    return parent[x]

def union_parent(parent, a, b, c) :
    global weight
    a_root = find_parent(parent, a)
    b_root = find_parent(parent, b)

    # if a < b :
    #     parent[b] = a
    # else :
    #     parent[a] = b
    # b 가 a보다 무게가 더 큰값이 들어오게 넣어야함
    if a_root != b_root :
        parent[b_root] = a_root # 무게가 가장 작은 것이 부모로 되게
        # 그럼 b의 무게는 a 보다 c 만큼 무겁겠다
        # weight[b] = weight[a] + c # 집합이 갑자기 묶이는 경우 반영이 안됨
        # weight[b_root] = c + (weight[b] - weight[a])
                            # 상대적인 값 반영 하기 위한.. 범위같은거
        weight[b_root] = c + (weight[a] - weight[b])
    # else : # 같으면
        # weight[b_root] += c + weight[a_root]

# 인덱싱으로 접근해야 시간 아낄 듯? 교수님은 기다리지 않는다고 함 -> 시간 잘..신경
# 무게 차이를 계산할 수 있다 -> 같은 집합으로 묶여있다.

while(True) :
    N, M = map(int, input().split())
    if N == 0 and M == 0 : break
    parent = [i for i in range(0, N + 1)]
    weight = [0 for i in range(100001)]

    for _ in range(M) :
        seq = list(input().rstrip().split()) # ['!', '1', '2', '1']
        # print(seq)
        # flag = False
        a = int(seq[1])
        b = int(seq[2])
        # c = int(seq[3]) # 무게 차이! # ? 일땐 없다...

        if seq[0] == '!' :
            # 무게 측정
            # 상대적인 것 끼리 계산을 하려면 서로 다 묶여있어야함
            # 즉, 무게 차이를 계산할 수 있다는 것은 같은 집합으로 묶여 있다는 것이다
            # union_parent(parent, a, b)
            union_parent(parent, a, b, int(seq[3]))
            # weight[b] = weight[a] + c  # 안묶이다가 갑자기 묶이면 값 반영 하기 힘듬
            # 최종 부모 노드로 부터 무게 값이 상대적으로 계산이 되어야함!

            # 합치지 않으면 계산을 안하게 되니
            # 계산하는걸 find에 추가해줘야함


        else :
            # 교수님 질문
            # 상대적인 무게를 계산하기 위해서는 같은 집합이어야함
            if find_parent(parent, a) == find_parent(parent , b) :
                # 무게 계산 할 수 있는 경우
                print( weight[b] - weight[a] )
            else :
                print("UNKNOWN")