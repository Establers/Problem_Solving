import sys

n = int(sys.stdin.readline().rstrip())

cnt = n  # 그룹 단어 개수 카운트

for _ in range(n) : 
    word = sys.stdin.readline().rstrip()   # 단어 입력 string

    for i in range(0, len(word)-1) : 
        if word[i] == word[i+1] :
            pass # 바로 옆이랑 값이 같으면 그냥 넘어가고...
        elif word[i] in word[i+1 : ] :   # 바로 옆 값이 다르면서, 그 이후에 있다면
            # print("값 다름")
            cnt = cnt - 1 # cnt 총량에서 감소
            break  # 그룹 단어가 아니라는 것이 확인 됐으니 지금 word에 대한 확인필요X
          
print(cnt)