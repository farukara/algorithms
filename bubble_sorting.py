#!python3
from numpy import random
from time import perf_counter

def buble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def main():
    a = random.randint(1_000, size=5_000)
    print(a)

    start = perf_counter()
    print(buble_sort(a))
    end = perf_counter()

    print(f"\nit took {(end-start):.2f} seconds to sort {len(a):,} items")


if __name__ == "__main__":
    main()

