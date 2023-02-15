import sys
input = sys.stdin.readline
import copy
# combination 안쓰고 풀기
# 무지성 bt

def backtracking(depth, li : list, idx) :
    global linum
    global visited

    if (depth == 6) :
        print(*li)
        return

    for i in range(idx, linum[0]) :
        if not visited[i] :
            li.append(num_list[i])
            visited[i] = True
            backtracking(depth + 1, li, i+1)
            li.pop()
            visited[i] = False

while(True) :
    linum = list(map(int, input().split()))

    if (linum[0] == 0):
        break

    num_list = copy.deepcopy(linum[1:])

    visited = [ False for _ in range(linum[0]+1)]

    backtracking(0,[],0)
    print(" ")




