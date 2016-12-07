import math

def insertion(nums):
    for i in range(1, nums.__len__()):
        tmp = nums[i]
        for j in range(i-1,-1,-1):
            if tmp < nums[j]:
                nums[j+1] = nums[j] # and nums[j] = tmp
                if j == 0:
                    nums[j] = tmp
            else:
                nums[j+1] = tmp
    
    return nums


def merge(A, p, q, r):
    L = A[p: q]
    L.append(math.inf)
    R = A[q: r]
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <=  R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def mergesort(A, p, r):
    if r == p + 1:
        return A
    else:
        q = p + (r - p) // 2
        A = mergesort(A, p, q)
        A = mergesort(A, q, r)
        A = merge(A, p, q, r)
        return A

def bubble(A):
    if len(A) == 1:
        return A
    for i in range(len(A)-1):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

nums = [5,4,3,2,1]
print("--"*16 + "\n" + "insertion")
print(insertion(nums[:])) #print(insertion(nums))

print("--"*16 + "\n" + "mergesort")
print(mergesort(nums[:], 0, len(nums))) #print(merge(nums, 0, 5, 5))

print(nums)
print("--"*16 + "\n" + "bubblesort")
print(bubble(nums[:]))
