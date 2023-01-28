nums = list(input().split("-"))
temp = 0
result = 0
max_value = 0
first_value = sum(list(map(int, nums[0].split("+"))))
# print(first_value)
# print(nums)
for i in nums[1:] :
    if i.isdigit() != True :
        temp = sum(list(map(int, i.split("+"))))
        max_value += temp

    else :
        max_value += int(i)


if len(nums) == 1 : # - 가 없을 경우
    print(first_value - max_value)
else :
    print(first_value - max_value)

