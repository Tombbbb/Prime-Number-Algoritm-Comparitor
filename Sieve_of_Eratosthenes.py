from math import sqrt
from math import floor

def Sieve_of_Eratosthenes(bound):
    nums = list(i for i in range(2,bound+1))##

    index = 0
    while True:
        value = nums[index]
        while True:
            value += nums[index]
            try:
                nums.remove(value)   
            except ValueError:
                if value > nums[-1]:
                    break
        index += 1
        try:
            nums[index]
        except:
            break

    return nums
