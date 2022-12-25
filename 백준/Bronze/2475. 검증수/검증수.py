import sys

def get_verify_num(list_num) : 
    for i in list_num :  
        value = [i*i for i in list_num]
        return sum(value) % 10

list_num = list(map(int, sys.stdin.readline().split()))

print(get_verify_num(list_num))
