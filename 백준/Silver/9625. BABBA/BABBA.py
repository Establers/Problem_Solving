# A -> B
# B -> BA
# 처음엔 A
# 버튼을 누를 수록
k = int(input())

# A
# B
# BA 1 1
# BAB 1 2
# BAB AB 2 3
# BAB BAB BA 3 5
# BA B BA BA B BA BA B 5 8
# BA B BA BA B BA B BA BA B BA B BA 8 13

arr_A = [1,0,1]
arr_B = [0,1,1]

if (k==0) :
    print(1, 0)
elif (k==1) :
    print(0, 1)
else :
    for i in range(2, k) :
        arr_A.append(arr_A[-2] + arr_A[-1])
        arr_B.append(arr_B[-2] + arr_B[-1])
    print(arr_A[-1], arr_B[-1])




