import sys
input = sys.stdin.readline

n = int(input())
dura = [0] * (n+1)
weight = [0] * (n+1)
result = 0

for i in range(1, n+1) :
    d, w = map(int, input().split())
    dura[i] = d
    weight[i] = w

def bt(depth) :
    #print(dura, depth)
    global result
    if (depth == n+1):
        #print("end")
        temp = 0
        for i in dura[1:] :
            if i <= 0 :
                temp += 1
        result = max(result, temp)
        return

    if(promising(depth)) :
        for i in range(1, n + 1):
            # 같은걸 hit 하려고 하면 continue
            if i == depth: continue
            # 깨진걸 hit 하려고 하면 다음꺼
            if dura[i] <= 0:
                continue

            dura[depth] -= weight[i]
            dura[i] -= weight[depth]
            #print(dura, depth, i)
            bt(depth + 1)

            dura[depth] += weight[i]
            dura[i] += weight[depth]
    else :
        bt(depth+1)

def promising(depth) :
    temp = 0
    for i in dura[1:] :
        if i == depth : continue
        if i <= 0 :
            temp += 1 # 깨진 것 갯
    if dura[depth] <= 0 or temp == len(dura[1:])-1 :
        return False
    else :
        return True

bt(1)
print(result)


