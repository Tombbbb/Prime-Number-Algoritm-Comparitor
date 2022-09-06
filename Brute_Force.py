from math import sqrt
from math import floor

def Brute_Force(bound):

    primes = []

    for num in range(2, (bound+1)):
        sq_root = floor(sqrt(num))
        check_var = True
        possible_factor = 2
    
        while possible_factor <= sq_root:
            if (num % possible_factor) == 0:
                check_var = False
                break
            possible_factor += 1
        if check_var == True:
            primes.append(num)

    return primes
