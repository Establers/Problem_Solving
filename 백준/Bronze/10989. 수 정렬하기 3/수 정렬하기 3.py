import sys
n = int(sys.stdin.readline())
list_ = [0] * 10001
for _ in range(n) :
    # list_.append(int(sys.stdin.readline()))
    num = int(sys.stdin.readline())
    list_[num] = list_[num] + 1

for i in range(0,10001) :
    if(list_[i] == 0) : continue
    for _ in range(list_[i]) :
        print(i)

# for i in range(0, 10001) :
#     if ( list_.count(i) == 0 )  : continue
#     for _ in range(list_.count(i)) :
#         print(i)

# list_.sort()
# print(*list_, sep='\n', end='')