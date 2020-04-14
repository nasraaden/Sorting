# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements, the last index should be sorted afterwards
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # the range is from to the right of the curent index to the end of the array
        for j in range(cur_index + 1, len(arr)):
            # if the next element is smaller than the number at the smallest index
            if arr[j] < arr[smallest_index]:
                # TO-DO: set the element in that index to smallest index
                smallest_index = j
        # if current index is smaller than smallest index
        if cur_index < smallest_index:
            # switch them
            arr[cur_index] = arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


my_list = [8, 2, 5, 7, 4, 9, 1, 6, 3]
selection_sort(my_list)
print(my_list)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # for the first number
    for i in range(0, len(arr) - 1):
        # for the second number, to the right of the first number
        for j in range(i + 1, len(arr)):
            # if the first number is bigger than the second number
            if arr[i] > arr[j]:
                # swap them
                arr[i], arr[j] = arr[j], arr[i]

    return arr


bubble_sort(my_list)
print(my_list)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
