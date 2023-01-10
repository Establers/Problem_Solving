n = int(input())
num = input()
# print(ord("a")) # 97
# print(ord("z")) # 122

result = 0
for i in range(n) :
    result += (ord(num[i])-96) * (31**i)

print(result % 1234567891)
