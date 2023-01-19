import sys
input = sys.stdin.readline

# 일관성 X NO
# 일관성 O YES

t = int(input())

def solution() :
    global n
    for j in range(n) :
        num = input().rstrip()
        temp.append(num)

    temp.sort()

    for a in range(n-1) :
        if temp[a] == temp[a+1][0:len(temp[a])] :
            return "NO"
    return "YES"


for i in range(t) :
    n = int(input())
    temp = []
    print(solution())

