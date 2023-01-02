import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) : # Test case 마다
    n, m = map(int, input().split())
    _list = list(map(int, input().split()))
    count = 0

    while True :
        # 최대값 보다 작을때, 최대값과 같을때로 구분
        if _list[0] < max(_list) : # 최대값 보다 작을 때
            _list.append(_list.pop(0))  # 앞에껄 빼고 뒤에다 추가
            m = m-1                # 내 순서는 한칸 땡겨짐
            if m < 0 :             # 근데 내가 최대값 보다 작으면 다시 맨뒤로 감
                m = len(_list) - 1 # 값 다시 설정

        elif _list[0] == max(_list) : # 최대값과 맨앞이 같을 때
            _list.pop(0)              # 인쇄를 함  
            count += 1      # 인쇄 카운트 +1
            m = m - 1       # 내 순서 땡겨짐
            if m < 0 :      # 내 순서를 땡겼는데 음수면 뽑힌거니까 이 때의 count 출력
                print(count)
                break


