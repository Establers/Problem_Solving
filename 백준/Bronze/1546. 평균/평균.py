import sys

subject = int(sys.stdin.readline())
list_scores = list(map(int, sys.stdin.readline().split()))

def fake_score(list_) :
    global subject
    return sum(list_) / max(list_) / subject * 100
    # subject 대신 len(list_) 해도 ?..

print(fake_score(list_scores))