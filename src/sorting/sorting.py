# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merge_arr = [0] * elements

    # Your code here
    L = arrA
    R = arrB
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            merge_arr[k] = L[i]
            i += 1
        else:
            merge_arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        merge_arr[k] = L[i]
        i += 1
        k += 1

    # Checking if any element was right
    while j < len(R):
        merge_arr[k] = R[j]
        j += 1
        k += 1

    return merge_arr


# TO-DO: implement the Merge Sort function below recursively

def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Finding the mid of the array
    L = arr[:mid]
    R = arr[mid:]

    L = merge_sort(L)
    R = merge_sort(R)

    arr = merge(L, R)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
