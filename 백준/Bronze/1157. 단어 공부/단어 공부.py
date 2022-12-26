import sys

word = sys.stdin.readline().rstrip().upper()  # Mississipi
# 대소문자 구분 X , 출력은 대문자로 하므로 대문자로 전부 변경

list_word = list(set(word))      # 중복제거, 리스트화
list_cnt = []
for i in list_word : # 리스트 각 요소에 대해
    list_cnt.append(word.count(i))  # 요소별 개수를 list_cnt 리스트에 추가 

# list_cnt 에서 최대값이 두개 이상이면 ? 출력
if list_cnt.count(max(list_cnt)) >= 2 : print ('?')
else : print(list_word[list_cnt.index(max(list_cnt))])
# 각 요소별 개수를 센 리스트에서 최대값의 인덱스를 확인하고 
# 그 값에 해당하는 걸 list_word 참조해 출력