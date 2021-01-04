def sort(arr, key):
    return __binary_search(arr, 0, len(arr) - 1, key)


def __binary_search(arr, low, high, key):
    mid = (low + high) // 2
    if low == high:
        return -1
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        return __binary_search(arr, mid + 1, high, key)
    else:
        return __binary_search(arr, low, high - 1, key)


