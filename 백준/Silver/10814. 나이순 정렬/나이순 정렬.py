n = int(input())
people = []

for i in range(1,n+1) : 
    age, name = map(str, input().split())
    age = int(age) # 캐스팅

    people.append((age, name))
    # [ [..] , [.]]
    
people.sort(key = lambda x : x[0])
# 값을 다 받으면 age를 기준으로 오름차순 정렬

for j in people : 
    print(j[0], j[1])
