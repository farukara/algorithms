#!python3
from numpy import random
from time import perf_counter

def selection_sort(array):
    "a is a list like iterable. returns sorted version of a"
    
    for i in range(len(array)):
        j = 1
        k=i
        while i+j<len(array):
            if array[i+j] < array[k]:
                k = i+j
            j+=1
        array[i], array[k] = array[k], array[i]
    
    return array

def selection_sort_withEAFP(array):
    "a is a list like iterable. returns sorted version of a"
    "also implements EAFP principle as opposed to naive method above"
    
    for i in range(len(array)):
        j = 1
        k=i
        #while i+j<len(array):
        controller = True
        while controller:
            try:
                if array[i+j] < array[k]:
                    k = i+j
                j+=1
            except IndexError:
                controller = False
        array[i], array[k] = array[k], array[i]
    
    return array

def main():
    a = random.randint(1000, size=5_000)
    print(a)
    start = perf_counter()
    print(selection_sort(a))
    print(f"naive selection: it took {(perf_counter() - start):.2f} "\
            f"seconds to sort {len(a):,} items\n")

    a = random.randint(1000, size=5_000)
    print(a)
    start = perf_counter()
    print(selection_sort_withEAFP(a))
    print(f"selection with EAFP: it took {(perf_counter() - start):.2f} "\
            f"seconds to sort {len(a):,} items")

if __name__ == "__main__":
    main()
