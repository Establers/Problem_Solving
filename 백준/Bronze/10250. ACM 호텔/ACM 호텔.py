t = int(input())

for i in range(t) : # 테스트 케이스만큼
    H, W, N = map(int, input().split())

    # 101 201 301 401 501 ... 102 202 층은 N % H 임을 알 수 있다.
    # 층 계산
    if (N % H == 0) : # 딱 떨어지는 경우는 0이 나와서 예외처리
        height = H
    else :
        height = N % H

    # 그럼 호는 아래 규칙을 통해, 한층을 반복해야 +1 되는것을 알수있음
    # 101 201 301 401 501 601 102 202 302 402 502 602
    if (N % H == 0) : # 같으면 바뀌지 않음 예외처리
        ho = N // H
    else :
        ho = N // H + 1

    # 출력
    if ho < 10 :
        print(str(height), "0",str(ho), sep='')
    else:
        print(height,ho,sep='')