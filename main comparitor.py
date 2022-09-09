from time import time
import matplotlib.pyplot as plt
from Brute_Force import Brute_Force
from Sieve_of_Eratosthenes import Sieve_of_Eratosthenes
#any future algorithms will need to be imported

def Algorithm_Selector(algorithm, bound):
    """
    This Subroutine secets and calls the alogrithm that finds prime numbers
    This subroutine make it easier adding additional algorithms to add in the future
    """
    if algorithm == "BruteForce":
        return Brute_Force(bound)
    elif algorithm == "SieveofEratosthenes":
        return Sieve_of_Eratosthenes(bound)

algorithms = ["BruteForce", "SieveofEratosthenes"] #list of all existing algorithms

while True: #Forces the user to enter a valid upper bound for the algorithm to work towards
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

colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k'] #up to 7 default colours included

for num in range(1000000, upper+1):
    times = [None]*len(algorithms)
    parity = [[]]*len(algorithms) #this is used to ensure all algorithms produce the same output
    for algorithm in algorithms:
        start = time() #gets UNIX time stamp before algorithm starts
        primes = Algorithm_Selector(algorithm, num)
        end = time() #gets UNIX time stamp after algorithm concludes
        index_value = algorithms.index(algorithm)
        times[index_value] = end - start #calculating and storing the runtime of the algorithm
        parity[index_value] = primes
    for i in range(len(parity)-1): #checks the parity of the different algorithms
        if parity[i] != parity[i+1]:
            print("ERROR: algorithms produced different outputs")
            print()

    for i in range(len(times)):
        plt.scatter(num, times[i],  facecolor="none", edgecolor=colours[i], marker="p") #plots the times

plt.show()
