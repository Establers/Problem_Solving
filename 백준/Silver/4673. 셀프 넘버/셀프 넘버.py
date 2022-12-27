def drkaprekar(n) :
    n = n + sum(map(int, str(n)))
    return n


list_not_selfnum = set()
# 생성자가 하나 이상 있는 수가 유일하지 않기에 중복된 값을 제거 위해 set (집합)으로 선언 

for i in range(1, 10001) : 
    list_not_selfnum.add(drkaprekar(i))

for k in range(1,10001) : 
    if k not in list_not_selfnum : 
        print(k)

# 집합에 들어있지 않는 것으로 출력

"""
list_selfnumber = [ i for i in range(1, 10001) ]
for i in range(1, 10001) :
    try : 
        list_selfnumber.remove(drkaprekar(i))
    except : continue

for k in list_selfnumber : 
    print(k)

    위 코드는 O(N^2) 로 추정되서 시간이 너무 느린 단점이 있음.
    remove 는 시간복잡도 N을  가지고 있다는 것을 모르고 작업을 했음.
"""


