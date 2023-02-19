import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

answer = 0

def bt(depth, str_ : str) :
    global answer
    if(depth == len(s)):
        if(str_ == s) :
            answer = 1
            return True
        else:
            return False

    if(str_[-1] == 'A') :
        if(bt(depth - 1 , str_[:-1])) : return True # A일 경우 짜르기
    if(str_[0] == 'B') :
        if(bt(depth - 1 , str_[1:][::-1])) : return True


if(bt(len(t), t)) :
    answer = 1

print(answer)