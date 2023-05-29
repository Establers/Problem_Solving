import sys
input = sys.stdin.readline
import heapq


n = int(input())
infos = dict()
answer = 0
for _ in range(n) :
    query = list(input().split())
    #print(query)
    if query[0] == '1' :
        if query[1] not in infos :
            hq = []
            for v in query[3:] :
                heapq.heappush(hq, -1 * int(v))
            # infos = {query[1]: hq}
            infos[query[1]] = hq
        else :
            for v in query[3:] :
                heapq.heappush(infos[query[1]], -1 * int(v))

    else : # 2
        #print(infos)
        if query[1] in infos :
            for i in range(int(query[2])) :
                if infos[query[1]] :
                    value = heapq.heappop(infos[query[1]])
                    #print(value)
                    answer += (-1 * value)

                else :
                    break

print(answer)