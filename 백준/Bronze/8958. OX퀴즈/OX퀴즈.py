
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) : 
    quiz = list(input())
    score = 0
    score_sum = 0
    for i in quiz : 
        if i == 'O' :
            score += 1
            score_sum = score_sum + score
        else : 
            score = 0
    print(score_sum)