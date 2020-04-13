# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            # TO-DO: swap
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if smallest_index != cur_index:
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


my_list = [8, 2, 5, 7, 4, 9, 1, 6, 3]
# selection_sort(my_list)
print(my_list)

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


bubble_sort(my_list)
print(my_list)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr

