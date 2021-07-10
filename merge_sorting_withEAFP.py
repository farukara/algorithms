#!python3
from numpy import random
from time import time
# *TODO can be improved for possible erronious inputs
# otherwise pretty happy.
# prioritizing left array in case of key equality makes the sort stable.

a = random.randint(1000, size=2000000)
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
        loop_constant = True
        while loop_constant:
            try:
            #while i < len(larray) and j < len(rarray):
                if larray[i] <= rarray[j]:
                    #print(f"i : {i}, in if")
                    sorted_array.append(larray[i])
                    i += 1
                else:
                    sorted_array.append(rarray[j])
                    #print(f"j : {j} in else")
                    j +=1
            except IndexError as e:
                #print(f"there is an error: {e}")
                if i == len(larray):
                    sorted_array.extend(rarray[j:])
                    loop_constant = False
                else:
                    sorted_array.extend(larray[i:])
                    loop_constant = False

    return sorted_array
    
if __name__ == "__main__":
    start = time()
    print(merge_sort(a))
    print(f"completed in {time() - start} sec")
