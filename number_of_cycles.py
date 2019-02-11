## This code finds out the number of cycles
#  in an array of indices i.e. an array whose
#  elements are the indices of that array. So,
#  an element of an array can point to another
#  element of the array, and if one of the next
#  elements in this manner point to a previous
#  element then that completes a cycle.
#  eg. [1, 2, 0, 4, 3, 5] this array has 3 cycles
#  [1, 2, 0], [4, 3] and [5] since element at
#  index 0 points to index 1 which then points
#  to index 2 which inturn points back to index 0.
##

def number_of_cycles(arr):
    # Write your code here
    c = 0
    j = 0
    cycle = []
    indices = range(0, len(arr))
    while len(indices)>0:
        j = indices[0]
        while True:
            cycle.append(j)
            j = arr[j]
            if j in cycle:
                c += 1
                for k in cycle:
                    indices.remove(k)
                cycle = []
                break
    return c


print(number_of_cycles([0,1,3,2,4]))
