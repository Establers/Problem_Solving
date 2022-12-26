import sys
temp = sys.stdin.readline().rstrip()

n = temp[:]

cnt = 0
temp_str = ''
temp_sum = 0

while True : 
    # 10 미만일 때 0 추가    
    if (int(temp) < 10) :
        temp = "0" + str(temp)[-1]

    # 합계산
    temp_sum = int(temp[0]) + int(temp[1])

    if int(temp_sum) < 10 : 
        temp_sum = "0" + str(temp_sum)[-1]

    # 구한 합으로 새로운 수 구현
    temp_str = str(temp)[1] + str(temp_sum)[1]

    # 새로운 수로 다시 위 과정 계산하기 위해 temp에 값
    temp = temp_str[:]
    # print(temp)
  
    cnt += 1
    if (int(n) == int(temp)) : 
        print(cnt) 
        break
    