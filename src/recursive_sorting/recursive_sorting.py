# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    index_a = 0  # starting with the smallest index for a
    index_b = 0  # starting with the smallest index for b
    # index_m = 0  # index to hold merged array
    # using a while loop, look at all the indices in both arrA and arrB
    # while index_a < len(arrA) and index_b < len(arrB):
    #     # look at each index of arrA and arrB, add smaller index to merged_arr
    #     if arrA[index_a] < arrB[index_b]:
    #         merged_arr[index_m] = (arrA[index_a])
    #         # increment arrA index and merged index so that it doesn't stop after first index
    #         # index_m += 1
    #         index_a += 1
    #     else:
    #         merged_arr[index_m] = (arrB[index_b])
    #         # index_m += 1
    #         index_b += 1
    # once arrA is finished, do the same for arrB
    # while index_a == len(arrA) and index_b < len(arrB):
    #     merged_arr[index_m] = (arrB[index_b])
    #     # index_m += 1
    #     index_b += 1

    # loop through elements in arrA and arrB and look at first index at arrA and arrB
    # add the smaller number at first of both arrays to merged arr
    # increment indices until both arrays have been added to merged_arr
    # return merged_arr
    for i in range(0, elements):
        if index_a >= len(arrA):
            merged_arr[i] = arrB[index_b]
            index_b += 1
        elif index_b >= len(arrB):
            merged_arr[i] = arrA[index_a]
            index_a += 1
        elif arrA[index_a] < arrB[index_b]:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            merged_arr[i] = arrB[index_b]
            index_b += 1
    return merged_arr


# arrA = [1, 2, 3, 10, 11, 12, 14]
# arrB = [4, 5, 6, 19, 25, 80]

# print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # check for base cases
    if len(arr) <= 1:
        return arr
    else:
        # left array is going to be from the start of the array to half of the length of the array
        left = merge_sort(arr[0:len(arr) // 2])
        # right array is going to be from where arrA ended to the end of the array
        right = merge_sort(arr[len(arr) // 2:])
        # in return, merge the two arrays
        # and call function on arrA and arrB since arr will keep dividing
        arr = merge(left, right)
    return arr


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
