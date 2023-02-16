import itertools

moum = ["a", "e", "i", "o", "u"]

L, C = map(int, input().split())
str_list = list(input().split())
str_list.sort()

# a..b...c..d..e 증가하는 순서로 넣어야 하고
# 최소 한개의 모음이 포함되어야 한다 + 두개의 자음

for perm_str in itertools.combinations(str_list, L) :
    count = 0
    for i in perm_str :
        if i in moum :
            count += 1

    if(count >= 1 and L-count >= 2) :
        print(*list(perm_str), sep='')