import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num_list = list(map(int, input().split()))
visited = [ False for _ in range(n) ]
num_list.sort()
def backtracking(depth, li : list, i) :
    if depth == m :
        print(*li, sep=' ')
        return


    for i in range(n):
        if not visited[i] :
            li.append(num_list[i])
            visited[i] = True
            backtracking(depth + 1, li, i)
            visited[i] = False
            li.pop()


backtracking(0, [], 0)