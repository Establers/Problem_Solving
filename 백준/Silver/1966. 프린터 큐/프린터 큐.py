import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) : # Test case 마다
    n, m = map(int, input().split())
    _list = list(map(int, input().split()))
    count = 0

    while True :
        if _list[0] < max(_list) :
            _list.append(_list.pop(0))
            m = m-1
            if m < 0 :
                m = len(_list) - 1

        elif _list[0] == max(_list) :
            _list.pop(0)  # 인쇄
            count += 1
            m = m - 1
            if m < 0 :
                print(count)
                break