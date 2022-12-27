import sys

cro = sys.stdin.readline().rstrip()
# string
cnt = 0
list_cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# dz= 와 z= 는 중복될 우려가 있음. dz=가 우선순위이기에 dz= 부터 체크

for word in list_cro : 
    cnt = cnt + cro.count(word)
    cro = cro.replace(word,' ')  # 검색한 값 제거
  
print (cnt + len(cro.replace(' ', ''))) # 공백 전체 제거