import  os
print(os.getcwd())
print(os.listdir())

f = open("LICENSE.txt")
f.readline()
# \n 이 나타나면 한 줄이 끝난 줄 알고 딱 멈춤

for x in range(5):
    f.readline()
# 여러 줄을 이렇게 출력하는 방법도 있지만

lines = f.readlines()  # readline 's'
print(lines[:2])
# ['A. HISTORY OF THE SOFTWARE\n', '==========================\n']
# readlines() 는 파일 읽은 것들을 한줄씩 각각 리스트의 원소로 들어가는 함수

# 출력을 원할 때
for l in lines[26:41]:
    print(l, end='')

# 끝에서 10줄을 출력하기
for l in lines[-10:-1] :
    print(l, end='')
