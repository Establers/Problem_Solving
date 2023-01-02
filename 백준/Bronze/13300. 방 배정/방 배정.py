
n, k = map(int, input().split())
male = [0 for _ in range(7)]
female = [0 for _ in range(7)]

# print(male)
for _ in range(n) :
    s, y = map(int, input().split())
    if (s == 1) :
        male[y] += 1
    else :
        female[y] += 1

for i in range(1, 7) :
    if female[i] % k == 0 :
        female[i] = female[i] // k
    else :
        female[i] = female[i] // k + 1

    if male[i] % k == 0 :
        male[i] = male[i] // k
    else :
        male[i] = male[i] // k + 1

print(sum(female) + sum(male))


