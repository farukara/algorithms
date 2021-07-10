#!python3
# 

from numpy import random
from math import log


def radix_sort(array):
    """radix sorts array if positive integers, uses counting sort as subroutine"""
    
    l = [[]]*10  #(max(array)+1)
    print("lll: ", l)
    for i in range(int(log(max(array),10))+1):
        modder = (10**i)
        print("modder: ", modder)
        for j in array:
            digit = (j//modder)%(modder*10)
            print("digit: ", digit)
            print("ldigit: ", l[digit])
            l[digit].append(j)
            print(l)
            break

def counting_sort(array):
    """sorts array using counting sort. 
    Respects original order when keys are equal"""

    l = [0]*(max(array)+1)
    for i in array:
       l[i] += 1
    l[-1] = len(a)-l[-1]
    for i in range(len(l)-2, 0, -1):
        l[i] = l[i+1] - l[i]

    sorted_array = [0]*(len(array))
    for i in a:
        sorted_array[l[i]] = i 
        l[i] +=1
    return sorted_array


def main():
    a = random.randint(100, size=10)
    print(a)
    print(radix_sort(a))

if __name__ == "__main__":
    main()
