import sys

list_ = []
for _ in range(10) :
    num = int(sys.stdin.readline().rstrip())
    list_.append(num % 42)
print(len(set(list_)))