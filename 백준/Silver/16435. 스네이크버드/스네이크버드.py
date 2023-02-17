import sys
input = sys.stdin.readline



def solution() :
    n, L = map(int, input().split())
    q = list(map(int, input().split()))

    q.sort()
    # print(q)
    for i in q :
        if i <= L :
            # eat
            L += 1

        else :
            print(L)
            return
    print(L)

solution()
