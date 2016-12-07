import numpy as np

def sortquick(A, l, r):
    if (l + 1 >= r):
        return A
    q = partition(A, l, r)
    sortquick(A, l, q-1)
    sortquick(A, q, r)
    return A

def partition(A, l, r):
    i = l-1
    for j in range(l, r):
        if (A[j] <= A[r-1]):
            i = i + 1
            A[i], A[j] = A[j], A[i]
    q = i + 1
    return q

array = np.random.random(5) * 10
# array = [5, 1, 1, 2, 3]
print(array)
print(sortquick(array[:], 0, len(array)))
