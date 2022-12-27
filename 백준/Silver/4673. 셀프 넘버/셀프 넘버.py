def drkaprekar(n) :
    n = n + sum(map(int, str(n)))
    return n

list_selfnumber = [ i for i in range(1, 10001) ]

for i in range(1, 10001) :
    try : 
        list_selfnumber.remove(drkaprekar(i))
    except : continue

print(*list_selfnumber, sep='\n')