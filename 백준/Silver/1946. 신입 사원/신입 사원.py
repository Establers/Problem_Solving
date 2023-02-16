import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t) :
    n = int(input()) # 사원 수
    people = []
    answer = 1
    for i in range(n) :
        a, b = map(int, input().split())
        people.append((a,b))

    people.sort(key = lambda x : x[0])

    #print(people)
    topA, topB = people[0][0], people[0][1]

    for a,b in people[1:] :
         if a <= topA or b <= topB :
             # 채용가능
             topA = a
             topB = b
             answer += 1

    print(answer)

    #top 에서 부터 둘다 높으면 X
    #둘 중 하나라도 낮으면 가능 -> 새로운 top

