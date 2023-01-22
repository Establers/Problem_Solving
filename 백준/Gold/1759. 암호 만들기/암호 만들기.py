import sys
import itertools
input = sys.stdin.readline

L, C = map(int, input().split())

chars = list(input().split())
chars.sort() # 알파벳 순을 위한 정렬

moum = ["a","e","i","o","u"]
result = []

def conca(list_) :
    temp = ''
    for i in list_ :
        temp += i
    return temp
    
for pw in itertools.combinations(chars, L) : 
    # 단어 선택 pw
    count = 0
    
    # 1. 단어 스펠링 하나하나를 보면서 모음인지 아닌지 확인 
    for i in pw : 
        if i in moum :
            count += 1 # 모음의 개수를 증가시킴
            
    if count >= 1 and count <= L-2 : # 이 단어가 조건을 만족하는지 ?
        # 맞다면
        # result.append(pw)
        # pw는 ('a', 't', 'c', 'i') 이런 형식의 값이니 변경 필요
        result.append(
            conca(list(pw))
        )

print(*result, sep='\n')
