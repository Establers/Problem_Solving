# 100 Comb 3   .. NC3
#

while True :
    num_list = list(map(int, input().split()))
    if num_list == [0,0,0] : break # 값 입력받기 멈추기 위함
    num_list.sort() # 맨 우측이 최대 값 # 크기 순 정렬을 함 
    if (num_list[2])**2 == (num_list[1]**2 + num_list[0]**2) : # c^2 = a^2 +b^2 이 만족해야 직각삼각형
        print("right")
    else :
        print("wrong")



