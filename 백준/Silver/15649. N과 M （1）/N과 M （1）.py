import sys
input = sys.stdin.readline

n, m = map(int , input().split())

def bt(depth, li) :
    if(depth == m) : #end
        print(*li)
        return
    else :
        for i in range(1, n+1) :
            if i not in li :
                li.append(i)
                bt(depth+1 , li)
                li.pop()

bt(0,[])