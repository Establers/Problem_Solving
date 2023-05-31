import sys
input = sys.stdin.readline
import heapq

n = int(input())    # 쿼리의 개수
infos = dict() 
# Query가 100000개, 종류도 100000개 라서 O(n) 탐색하면 안되기에 O(1) 탐색을 하기위해
# Hash 구조를 가진 자료구조 사용 {key : value}

answer = 0
for _ in range(n) : 
    query = list(input().split())
    # ['1', 'java', '2' ....]

    if query[0] == '1' : 
        if query[1] not in infos : # java가 infos에 없다면 새로 등록해줌 
            hq = []                 # 힙자료구조
            for v in query[3:] :    # 정보
                heapq.heappush(hq, -1 * int(v)) 
                # 최소 힙에 -를 곱하고 넣은 다음에 뽑고 나서 다시 -를 취하면 최대힙 처럼 동작
            
            infos[query[1]] = hq # java 에 heapq 자료구조 넣음
        else :
            # 이미 해당 이름이 있을 경우
            for v in query[3:] :
                heapq.heappush(infos[query[1]], -1 * int(v))
                # 힙큐에 값을 추가로 넣어 준다.

    else : # 2 
        if query[1] in infos :
            for i in range(int(query[2])) :
                if infos[query[1]] : # 힙에 값이 남아있다면
                    value = heapq.heappop(infos[query[1]])
                    # 힙에서 자료를 뽑은 뒤, -1을 곱하고 정답에 넣어준다.
                    answer += (-1 * value)

                else : # 값이 없다면 이번 쿼리를 끝낸다.
                    break

print(answer)