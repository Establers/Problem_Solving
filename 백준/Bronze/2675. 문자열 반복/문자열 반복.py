import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T) : 
    counts, words = input().split()
    for x in words : 
        print(x*int(counts), end='')
    print()