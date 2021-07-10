#!python3
import time
from numpy import random
#import concurrent.futures
import multiprocessing

def merge(larray, rarray):
    i=j=0
    sorted_array = []
    while i < len(larray) and j < len(rarray):
        if larray[i] <= rarray[j]:
            sorted_array.append(larray[i])
            i += 1
        else:
            sorted_array.append(rarray[j])
            j +=1
    if i == len(larray):
        sorted_array.extend(rarray[j:])
    else:
        sorted_array.extend(larray[i:])

    return sorted_array
    
def merge_sort(array):
    if len(array) <= 1:
        return array

    if len(array) > 1:
        larray, rarray = array[:len(array)//2], array[len(array)//2:]
        larray = merge_sort(larray)
        rarray = merge_sort(rarray)
        
        return merge(larray, rarray)

def parallelit(array):
    nofpros = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=nofpros)
    chunk = len(array)//nofpros
    data = [array[i*chunk:(i+1)*chunk] for i in range(nofpros)]
    data = pool.map(merge_sort, data)
    extra = data.pop() if len(data) % 2 == 1 else None
    print(data)
    for i in range(nofpros//2):
        for j in range(0, len(data), 2):
            data[i] = merge(data[j], data[j+1])
    if extra:
        data = merge(data, extra)

    return data[0]

def main():
    a = list(random.randint(1000, size=1_000_000))
    #print(a)
    start = time.time()
    #a = parallelit(a)
    print(parallelit(a))
    finish = time.time()
    print(f"\nit took {(finish-start):.2f} seconds to sort {len(a):,} items.")

if __name__ == "__main__":
    main()
