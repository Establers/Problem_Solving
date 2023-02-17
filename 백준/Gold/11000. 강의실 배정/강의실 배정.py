import sys
input = sys.stdin.readline
import heapq

n = int(input())
sooup = []

for i in range(n) :
    sooup.append(list(map(int, input().split())))

sooup.sort(key = lambda x : (x[0], x[1]))

# print("정렬된 수업", sooup)
q = []
#  [1, 8], [3, 7], [5, 6], [6, 11], [8, 10], [9, 16], [10, 14], [11, 12]
heapq.heappush(q, sooup[0][1])
#print(q)
for i in sooup[1:] :
    if q[0] > i[0]:
        # 다음 수업의 시작 시간이 q[0](제일 빨리 끝나는 시간)
        # 보다 작을 경우, 수업을 중단 시킬 순 없으니
        # 새로운 수업으로 추가해줌 (끝나는 시간 추가)
        heapq.heappush(q, i[1])
    else :
        # 다음 수업 시작 시간이 q[0] 제일 빨리 끝나는 시간보다 같거나 크면
        # 바로 그 교실에서 이어서 할 수 있다는 것이고
        # 제일 빨리 끝나는 수업을 끝내버리고
        # 새로운 수업을 추가해줌
        heapq.heappop(q)
        heapq.heappush(q, i[1])


print(len(q))


