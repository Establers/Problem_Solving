import sys
input = sys.stdin.readline

n = int(input())    # 플레이어 수
players = [-1 for _ in range(1000001)]
numbers = list(map(int, input().split()))
scores = [0 for _ in range(n)]

for i in range(n) :
    players[numbers[i]] = i
# players 라는 리스트에
# numbers값으로 players 리스트 주소를 선택
# 넣은 numbers값 순서대로 리스트 주소 0 1 2 3 4 ...

for i in range(n) : # 모든 n에 대해
    for j in range(2*numbers[i], 1000001, numbers[i]) :
    # 자기자신의 값을 제외하고 내 배수만큼 조사를 하는데
        # numbers[i] 가 7 이라면
        # 14 21 28 ... 값을 players 리스트로 확인
        if players[j] >= 0 : # -1 이상(즉 14 21 28.. 등에 값이 있다면)
            scores[players[j]] -= 1
            # players[j]에는 무수히 많은 -1 과 0~n-1까지 인덱스를 나타내는 값들만 있고
            # 그 인덱스에 해당하는 값의 score 값을 감소 시키고
            scores[i] += 1
            # 그 인덱스에 해당하는 값의 score 값을 증가시킴

print(*scores, sep=' ')

