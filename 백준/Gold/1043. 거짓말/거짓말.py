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

N, M = map(int, input().split())
# parent = [0] *(N+1)]
parent = [ i for i in range(0, N+1)]
answer = 0
seq = list(map(int, input().split()))
# 진실을 아는 사람의 수 , 그 사람 번호
# 얘네와 같이 묶여있으면, 거짓말을 할 수 없다.
if(seq != 0) :
    for i in range(1, len(seq)-1) :
        # 3 1 2 7 ... len = 4
        union_parent(parent, seq[i], seq[i+1])

# M에 대해
# 하나하나 유니온 합치기
party_list = []
for _ in range(M) :
    party_seq = list(map(int, input().split()))
    party_list.append(party_seq)

    if party_seq[0] >= 2 :
        for i in range(1, len(party_seq) - 1) :
            union_parent(parent, party_seq[i], party_seq[i+1])

if seq != [0]:
    truth = find_parent(parent, seq[1])
else:
    truth = 10000


for party in party_list :
    b = find_parent(parent, party[1])

    if truth != b :
        answer += 1

print(answer)