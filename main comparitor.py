from time import time
import matplotlib.pyplot as plt
from Brute_Force import Brute_Force
from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes


def Algorithm_Selector(algorithm, bound):
    if algorithm == "BruteForce":
        return Brute_Force(bound)
    elif algorithm == "SieveofEratosthenes":
        return Sieve_of_Eratosthenes(bound)


while True:
    try:
        upper = int(input("enter upper bound: "))
    except:
        print("please enter an integer")
        continue
        
    if not upper > 0:
        print("please enter a positive integer")
        continue
    break

plt.figure(figsize=(7, 5))

algorithms = ["BruteForce", "SieveofEratosthenes"]
colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for num in range(2, upper+1):
    times = [None]*len(algorithms)
    parity = [[]]*len(algorithms)
    for algorithm in algorithms:
        start = time()
        primes = Algorithm_Selector(algorithm, num)
        end = time()
        index_value = algorithms.index(algorithm)
        times[index_value] = end - start
        parity[index_value] = primes
    for i in range(len(parity)-1):
        if parity[i] != parity[i+1]:
            print("ERROR: algorithms produced different outputs")
            print()

    for i in range(len(times)):
        plt.scatter(num, times[i],  facecolor="none", edgecolor=colours[i], marker="p")

plt.show()
