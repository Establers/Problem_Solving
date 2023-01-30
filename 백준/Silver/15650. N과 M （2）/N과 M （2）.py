
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = [i for i in range(0,n+1)] # 숫자1:1매칭
visited = [False for i in range(n+1)]

def bt(result) :

    if(len(result) == m):
        print(*result)
        return

    for i in range(1, n+1) :
        if(visited[i] == False) :
            if not result  or result[-1] < i:
                visited[i] = True
                result.append(i)
                bt(result)
                #
                visited[i] = False
                result.pop()

bt([])


