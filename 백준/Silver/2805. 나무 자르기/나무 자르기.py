import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n 나무 수 m 나무 길이
array = list(map(int, input().split()))
result = 0
start = 0
end = max(array)

while start <= end :
    total = 0
    mid = (start + end) // 2

    # 나무 길이 계산
    for x in array :
        if x > mid :
            total = total + (x-mid)
        else :  # 자를 수가 없는 경우
            pass

    if total < m :  # 나무 길이가 부족할 때
        end = mid - 1 # 끝값 재설정
    else :  # 나무길이가 더 남을 때  / 문제의 조건에 일단 만족하는 경우임
        result = mid    # 이 때의 자른 기준값을 일단 result에 저장
        start = mid + 1 # 시작값 재설정, total 이 더 작아질 수 있게하는 방향으로

print(result)
