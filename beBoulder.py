#Be Boulder

def testIfPartitioned(a, k):
    # TODO : test if all elements at indices < k are all <= a[k]
    #         and all elements at indices > k are all > a[k]
    # return TRUE if the array is correctly partitioned around a[k] and return FALSE otherwise
    assert 0 <= k < len(a)
    for i in range(0,len(a)):
        i = i 
        k = k 
        element = a[i]
        pivot = a[k]
        if i < k and a[i] > a[k]:
            return False
        elif i > k and a[i] < a[k]:
            return False
    return True
    
# assert testIfPartitioned([-1, 5, 2, 3, 4, 8, 9, 14, 8, 23],5) == False, ' Test # 5 failed.'

#%%
def swap(a, i, j):
    assert 0 <= i < len(a), f'accessing index {i} beyond end of array {len(a)}'
    assert 0 <= j < len(a), f'accessing index {j} beyond end of array {len(a)}'
    a[i], a[j] = a[j], a[i]

def tryPartition(a):
    # implementation of Lomuto partitioning algorithm
    n = len(a)
    pivot = a[n-1] # choose last element as the pivot.
    i,j = 0,0 # initialize i and j both to be 0
    for j in range(n-1): # j = 0 to n-2 (inclusive)
        # Invariant: a[0] .. a[i] are <= pivot
        #            a[i+1]...a[j-1] are > pivot
        #test if i is == n, this will happen if the array is already sorted 
        #   ascending
        if a[j] <= pivot: 
            swap(a, i, j)
            i = i + 1
    if i == n-1:
        return i
    else:
        swap(a, i, n-1) # place pivot in its correct place.
    return i+1 # return the index where we placed the pivot

a1 = [1,2,3]
a2 = [3,2,1]
a3 = [8,4,8,4,7,2,5]
a4 = [8,8,8,8,8,8,8]

one = tryPartition(a1)
two = tryPartition(a2)
three =tryPartition(a3)
four = tryPartition(a4)

