import random

textFile = open('ko_en.txt', "r",encoding='UTF8')

_dict = dict()

for line in textFile.readlines()[1:] :  # ko en 말고 다음꺼 부터
    kor, eng = list(line.split("\t"))   # \t 으로 구분되어 있다.
    _dict[kor] = eng    # 딕셔너리 형태를 구성한다.

quiz = list(_dict.keys())
random.shuffle(quiz)

while True :
    if len(quiz) == 0 : break
    print("Write  the following sentence in English.")

    q = quiz.pop()
    print(q)
    ans = input("\nyour answer: ")
    if ans == _dict[q].rstrip() :
        print('\nresult: Correct!')
    else:
        print("\nresult: Not correct!")
        print("right answer:" + _dict[q].rstrip() + '\n')

    print('-' * 80)
