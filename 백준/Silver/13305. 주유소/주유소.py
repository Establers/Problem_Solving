import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

money = 0
moving_dist = 0
result = 0

money = price[0]
moving_dist = 0

for i in range(1, len(price)) :
    #print(price[i])
    if price[i] <= money :
        #print(moving_dist, money)
        #print("도착 했을 때 ")
        moving_dist += dist[i-1]
        result += moving_dist*money
        money = price[i]
        moving_dist = 0
    else :
        #print("거리 : ", dist[i-1])
        moving_dist += dist[i-1]

print(result)