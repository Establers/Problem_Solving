import sys
input = sys.stdin.readline

# def fibonacci(num) :
#     global count0, count1
#
#     if (num == 0) :
#         count0 += 1
#         return 0
#     elif num == 1 :
#         count1 += 1
#         return 1
#     else :
#         return fibonacci(num-1) + fibonacci(num-2)

t = int(input()) # test case

for i in range(t) :
    n = int(input())

    list_zero = [1, 0]
    list_one = [0, 1]

    if n == 0 :
        print(1, 0)
    elif n == 1 :
        print(0, 1)

    if n >= 2 :
        for k in range(n-1) :
            list_zero.append(list_zero[-1] + list_zero[-2])
            list_one.append(list_one[-1] + list_one[-2])

        print(list_zero[-1], list_one[-1])


