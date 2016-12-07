import math
import numpy as np

def maxsublist(A, low, high):
    if (high - low == 1):
        return low, high, A[low]
    mid = (low + high) // 2
    left_low, left_high, left_max = maxsublist(A, low, mid)
    right_low, right_high, right_max = maxsublist(A, mid, high)
    mid_low, mid_high, mid_max = maxcrossingsublist(A, low, high, mid)

    if left_max >= right_max and left_max >= mid_max:
        return left_low, left_high, left_max
    elif right_max >= left_max and right_max >= mid_max:
        return right_low, right_high, right_max
    else:
        return mid_low, mid_high, mid_max


def maxcrossingsublist(A, low, high, mid):
    left_max = -math.inf
    if (high - low == 2):
        left_max = sum(A[low:high])
        return low, high, left_max
    
    mid_high = mid + 1
    mid_low = mid-1
    left_sum = 0
    for i in range(mid-1, low-1, -1):
        left_sum += A[i]
        if left_sum >= left_max:
            left_max = left_sum
            mid_low = i

    right_max = -math.inf
    right_sum = 0

    
    for i in range(mid, high):
        right_sum += A[i]
        if right_sum >= right_max:
            right_max = right_sum
            mid_high = i+1

    return mid_low, mid_high, left_max + right_max



def anotherversion(A):
    if (len(A) == 1):
        return 0, 1, A[0]
    max_array = A[0]
    max_array_special = A[0]
    low, high = 0, 1
    low_special, high_special = 0, 1
    for i in range(1, len(A)):
        high_special = i + 1
        if (max_array_special >= 0):
            max_array_special += A[i]
        else:
            max_array_special = A[i]
            low_special = i

        if (max_array < max_array_special):
            max_array = max_array_special
            low, high = low_special, high_special

    return low, high, max_array



A = np.random.random(10) - 0.5 # A = [1, -1, 2, 2, 1, -3, 5, 2, -5 ,5, -6]
print("=="*20)
print("A is:")
print(A)
print("=="*20)
print("divide and conquer:")
print(maxsublist(A[:], 0, len(A)))
print("=="*20)
print("non-recursion and line algorithm:")
print(anotherversion(A[:]))
