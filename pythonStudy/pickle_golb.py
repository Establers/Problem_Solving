users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open('users', 'wb')
import pickle
pickle.dump(users, f)
f.close()

import os
print(os.path.exists('users'))
# True

f = open('users', 'rb')
a = pickle.load(f)
print(a)

# 피클 모듈은 파이썬에서 만들어지는 모든 것을 기록? 불러올 수 있다??
from glob import glob
print(glob('*.exe'))    # 현재 디렉터리의 .exe 파일을 리스트 형태로 리턴을 함
print(glob('*.txt'))
print(glob(r'C:\U*'))