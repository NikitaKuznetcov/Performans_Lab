import math
from operator import index


nums = [1, 10, 2, 9]
result_digit = math.ceil((max(nums))/2) 
count = 0
for index, i in enumerate(nums):
    while i != result_digit: 
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
             i -= 1
             count += 1
        else:
            nums[index] = i
    print(count)