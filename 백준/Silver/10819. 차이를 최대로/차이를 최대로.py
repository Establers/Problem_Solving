import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
seq.sort()
visited = [False] * n
result = 0
answer = 0

def bt(depth, nums : list) :
    global answer
    global result

    if depth == n :
        #print(nums)
        result = 0
        for i in range(n-1) :
            result += abs(nums[i]- nums[i+1])
            #print(result)

        answer = max(answer, result)
        return

    for i in range(n) :
        if not visited[i] :
            nums.append(seq[i])
            visited[i] = True
            bt(depth + 1, nums)
            visited[i] = False
            nums.pop()

bt(0,[])
print(answer)