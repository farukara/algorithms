#!python3
from numpy import random
from time import perf_counter
# *TODO can be improved for possible erronious inputs
# otherwise pretty happy.
# prioritizing left array in case of key equality makes the sort stable.

a = random.randint(1_000, size=2_000_000)
print(a)

def merge_sort(array):
    if len(array) <= 1:
        return array

    if len(array) > 1:
        larray, rarray = array[:len(array)//2], array[len(array)//2:]
        larray = merge_sort(larray)
        rarray = merge_sort(rarray)
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
    
if __name__ == "__main__":
    start = perf_counter()
    print(merge_sort(a))
    print(f"\nsorted {len(a):,} items in {(perf_counter() - start):.2f} seconds")
