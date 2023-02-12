import sys
input = sys.stdin.readline

# 조합을 쓰는 경우 쉽게 끝나기 때문에
# Combination을 쓰지 않고 풀이하겠음

N, teamMember = map(int, input().split())
membersSolveList = []
result = 11

for i in range(teamMember) :
    solveList = list(map(int, input().split()))
    membersSolveList.append(solveList[1:])

# print(membersSolveList)
choiceMember = []
for i in range(1, 1<<teamMember) : # 공집합 제거 위해 1부터
    for j in range(0,teamMember) :
        if(i & (1<<j)) != 0 :
            choiceMember.append(j)
    # print(choiceMember)
    # 고른 멤버 확정 : 풀 수 있는 문제인지 확인
    # print(choiceMember)
    if(len(choiceMember) >= result) : # 이미 고른 사람이 지금 보다 더 많다면 psss
        choiceMember.clear()
        continue # 다음 멤버 선택
    ans = 0
    for mem in choiceMember :
        for pb in membersSolveList[mem] :
            ans = (ans | 2**(pb-1))
    if ((2**N-1) &(~ans) == 0) :
        # print("SOLVE", choiceMember)
        result = min(result, len(choiceMember))

    # 계산해봤으니 리스트 초기화
    choiceMember.clear()

if (result != 11) :
    print(result)
else :
    print(-1)