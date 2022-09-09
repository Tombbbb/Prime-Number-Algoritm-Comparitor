from math import sqrt
from math import floor

def Sieve_of_Eratosthenes(bound):
    nums = list(i for i in range(2,bound+1)) #produces list of numbers upto the largest number

    index = 0
    while index < len(nums):
        value = nums[index]
        while value <= nums[-1]:
            value += nums[index]
            try:
                nums.remove(value)   
            except ValueError:
                pass
        index += 1

    return nums
