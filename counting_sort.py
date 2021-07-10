#!python3
# this is counting sort, preserving original order of equal keys

from numpy import random

a = random.randint(1000, size=4000000)
print(a)

def counting_sort(array):
    """sorts array using counting sort. 
    Respects original order if keys are equal"""

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

print(counting_sort(a))
