# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    index_a = 0  # starting with the smallest index for a
    index_b = 0  # starting with the smallest index for b
    index_m = 0
    # using a while loop, look at all the indices in both arrA and arrB
    while index_a < len(arrA) and index_b < len(arrB):
        # look at each index of arrA and arrB, add smaller index to merged_arr
        if arrA[index_a] < arrB[index_b]:
            merged_arr[index_m] = (arrA[index_a])
            # increment arrA index so that it doesn't stop after first index
            index_m += 1
            index_a += 1
        else:
            merged_arr[index_m] = (arrB[index_b])
            index_m += 1
            index_b += 1
    while index_a == len(arrA) and index_b < len(arrB):
        merged_arr[index_m] = (arrB[index_b])
        index_m += 1
        index_b += 1

        # check for the smallest value at index 0 of both array
        # replace that value at index 0 of merged_arr
        # increment until you get to the last index of both arrays
    return merged_arr


arrA = [1, 2, 3]
arrB = [4, 5, 6]

print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # check for base cases
    if len(arr) <= 1:
        return arr
    # left array is going to be from the start of the array to half of the length of the array
    arrA = (arr[len(arr) // 2:])
    # right array is going to be from where arrA ended to the end of the array
    arrB = (arr[:len(arr) // 2])
    # merge the two arrays
    # merge(arrA, arrB)
    return merge(merge_sort(arrA), merge_sort(arrB))


arr = [8, 2, 5, 7, 4, 9, 1, 6, 3]
print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
