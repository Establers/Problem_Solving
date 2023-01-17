import sys
input = sys.stdin.readline

def find_num() :
    n, k = map(int, input().split())
    # k번째 지우게 되는 수
    count = 0
    array = [True for i in range(n + 1)]

    for i in range(2, n+1):
        if array[i] == True :
            for j in range(i, n+1, i) :
                if array[j] == True :
                    array[j] = False
                    count += 1
                    if (count == k) :
                        return j

print(find_num())
