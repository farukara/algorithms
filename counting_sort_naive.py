#!python3
# this is naive unstable counting sort, meaning:
# it does not preserve original order when keys are the same

from numpy import random

a = random.randint(1_000, size=4_000_000)

def naive_counting_sort(array):
    """sorts array without respecting original order when keys are equal"""

    l = [0]*(max(array)+1)
    for i in array:
       l[i] += 1
    sorted_array = []
    for i in range(len(l)):
        if l[i] != 0:
            sorted_array.extend([i]*l[i])

    return sorted_array

if __name__ == '__main__':
    print(naive_counting_sort(a))
