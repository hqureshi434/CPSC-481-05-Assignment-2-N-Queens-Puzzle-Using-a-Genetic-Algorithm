"""
Henry Torres
Ricky Martinez
Hammad Qureshi
"""
from timer import Timer
import random
from search import *

if __name__ == "__main__":
    newInput = int(input("Please enter a number of queens: "))
    print()
    t = Timer()
    t.start()
    nq = NQueensProblem(newInput)
    print("** GENETIC SEARCH **\n")
    print(genetic_search(nq))
    t.stop()
    print()