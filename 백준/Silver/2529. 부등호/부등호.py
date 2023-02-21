import sys
input = sys.stdin.readline

n = int(input())
seq = input().split()
answer_min = "10000000000"
answer_max = "0"



visited = [False] * 10

def promising(seq, nums) :
    count = 0
    for i in range(len(nums)-1) :
        if seq[i] == '>' :
            if nums[i] > nums[i+1] :
                #print(seq[i])
                count += 1
            else : return False
        else : # <
            if nums[i] < nums[i+1] :
                #print(seq[i])
                count += 1
            else : return False

    if count == len(nums) - 1 :
        #print("pro 체크 O")
        return True



def bt(depth, nums : list) :
    global seq
    global answer_min
    global answer_max

    if(promising(seq, nums)) :
        if depth == n + 1:
            temp_str = ""
            #print(nums)
            # 리스트를 숫자화 하기
            for i in nums:
                temp_str += str(i)
            temp_int = int(temp_str)

            answer_max = str(max(int(answer_max), temp_int))
            answer_min = str(min(int(answer_min), temp_int))
            if len(answer_min) + 1 == len(answer_max) :
                answer_min = "0" + answer_min
            return


        for i in range(0, 10) :
            if not visited[i] :
                nums.append(i)
                visited[i] = True
                bt(depth + 1, nums)
                visited[i] = False
                nums.pop()

    elif(len(nums) < 2) :
        for i in range(0, 10):
            if not visited[i] :
                nums.append(i)
                visited[i] = True
                bt(depth + 1, nums)
                visited[i] = False
                nums.pop()

bt(0, [])
print(answer_max)
print(answer_min)