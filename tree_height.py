# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    augstums = [-1] * n

    def aprekinat_augstumu(elements):
        if augstums[elements] != -1:
            return augstums[elements]
        if parents[elements] == -1:
            augstums[elements] = 1
        else:
            parent_h = aprekinat_augstumu(parents[elements])
            augstums[elements] = parent_h + 1
        return augstums[elements]


    max_height = 0
    for x in range(n):
        max_height = max(max_height, aprekinat_augstumu(x))
    return max_height


def main():
    # implement input form keyboard and from files
    text = input()
    if "I" in text:
        skaits = int(input())
        elementi = list(map(int ,input().split()))
        
    if "F" in text:
        nosaukums = input()
        nosaukums = "./test/"+ nosaukums
        with open(nosaukums, 'r') as dati:
            skaits = int(dati.readLine())
            elementi = list(map(int , dati.readLine().split()))
    print(compute_height(skaits, elementi))

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))