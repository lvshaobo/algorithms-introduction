import numpy as np

def binary(A, target, l, r):
    m = (l + r) // 2
    if (l == r):
        return None
    if (l + 1 == r):
        if (A[l] == target):
            return l
        else:
            return None
    if (A[m] == target):
        return m
    elif (A[m] > target):
        t = binary(A, target, l, m)
    else:
        t = binary(A, target, m+1, r)
    return t

A = np.random.randint(10, size=5)
A = np.sort(A)
print(A)
print(binary(A, 7, 0, len(A)))
