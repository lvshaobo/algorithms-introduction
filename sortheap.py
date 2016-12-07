import numpy as np
import copy

def heapify(A, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if (l < len(A) and A[l] > A[i]):
        largest = l
    if (r < len(A) and A[r] > A[largest]):
        largest = r
    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)
    return A

def buildheap(A):
    if (len(A) == 1):
        return A
    for i in range(len(A)//2 -1, -1, -1):
        A = heapify(A, i)
    return A

def sortheap(A):
    B = buildheap(A)
    for i in range(len(B)-1, 0, -1):
        B[i], B[0] = B[0], B[i]
        B[:i] = heapify(B[:i], 0)
    return B

# A = np.random.random(5) - 0.5 
A = [1, -1, 2, 2, 1, -3, 5, 2, -5 ,5, -6]
print(A)
# B = copy.copy(A)
print(sortheap(A[:]))
print(A)

