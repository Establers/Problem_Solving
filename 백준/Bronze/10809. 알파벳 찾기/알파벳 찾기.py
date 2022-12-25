import sys

word = sys.stdin.readline().rstrip()
# word = "baekjoon"

# print(word.find("a"))
# print(word.find("b"))

# print(ord("a"))  # 97 
# print(ord("z"))  # 122

for index in range(97, 123) :    # 97 a 122 z
    print(word.find(chr(index)),end=' ')