import sys
input = sys.stdin.readline

n = int(input())
seq = []

for i in range(n):
    a, b = map(int, input().split())
    seq.append((a,b))


seq.sort(key = lambda  x : (x[1],x[0]))
#print(seq)


answer = 0

now_a = seq[0][0]
now_b = seq[0][1]
count = 1
for a,b in seq[1:]:
    if a >= now_b :
        now_a = a
        now_b = b
        #print(now_a, now_b)
        count += 1

print(count)




