import sys

num_list = list(map(int, sys.stdin.readline().rstrip().split()))

list_sort = num_list.copy()
list_reverse = num_list.copy()

list_sort.sort()
list_reverse.sort(reverse=True)

# print(list_sort)
# print(list_reverse)

if (list_sort == num_list) :
    print("ascending")
elif (list_reverse == num_list) :
    print("descending")
else : print("mixed")