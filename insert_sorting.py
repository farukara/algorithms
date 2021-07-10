#!python3
from numpy import random
from time import perf_counter

def insert_sort(a):
    "a is a list like iterable. returns sorted version of a."

    for i in range(len(a)-1):
        for j in range(i+1):
            if a[i+1-j] < a[i-j]:
                a[i-j], a[i-j+1] = a[i-j+1], a[i-j]

def main():
    a = random.randint(1000, size=3_000)
    #a = [1,2,9,4,7,3,6,11,10]
    print(a)
    start = perf_counter()
    insert_sort(a)
    print(a)
    print(f"\nSort time for {len(a):,} items: {(perf_counter()-start):.2f} seconds\n")

if __name__ == "__main__":
    main()
