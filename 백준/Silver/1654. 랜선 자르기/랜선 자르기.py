import sys
input = sys.stdin.readline

K, N = map(int, input().split())
_list = []
for i in range(K) :
    _list.append(int(input()))
    
min_value = 1
max_value = max(_list)

while min_value <= max_value :          # 이분 탐색 완료까지
    mid = (min_value + max_value) // 2  # 이분 탐색을 위한 중간값 설정
    count = 0   # 개수를 담을 변수 (랜선을 자른 수)
    for i in _list :    # 리스트에 대해 각 선들 자른 수의 합을 구하기
        count += i // mid
    
    if (count >= N) :   # 자른게 N 보다 많으면
        min_value = mid + 1 # 중간값 +1 만큼 min_value를 증가
    else : 
        max_value = mid - 1 # 랜선의 최대 길이를 중간값보다 1작게 설정

print(max_value)


"""
start = max(_list)
end = 0
length = 0
Flag = False

# i 길이 최소 값에서 시작 그래야 선을 다 자를 수 있으니
for i in range(start,end,-1) :
    if start > end :
        return end

    count = 0              # count 자를 수 있는 선의 총합
    if Flag == True and length > i :
        break
    for j in _list :       # j 각 선들의 길이
        count += j // i    # 선을 잘라 나오는 개수
    if (count >= N) :      # 잘라서 나온게 N개 보다 많으면
        length = max(length, i) # 길이를 비교해 긴 것으로 갱신
        Flag = True

print(length) # 답을 구했지만 완전탐색이라 ㅜㅜ
"""