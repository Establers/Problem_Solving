import sys

H, M = map(int, sys.stdin.readline().split())
# 0-23, 0-59

# 45분 감소.

if(M < 45) : 
    M += 15 # 60 - 45 
    if (H == 0) : H = 23
    else : H = H - 1
else : M = M - 45

print(f'{H} {M}')