def sort(arr):
    __merge_sort(arr, 0, len(arr) - 1)
    return arr


def __merge_sort(arr, left, right):
    if left != right:
        q = (left + right) // 2
        __merge_sort(arr, left, q)
        __merge_sort(arr, q + 1, right)
        __merge(arr, left, q, right)


def __merge(arr, left, q, right):
    n1 = q - left + 1
    n2 = right - q
    l_arr = [0] * n1
    r_arr = [0] * n2
    for i in range(0, n1):
        l_arr[i] = arr[left + i]
    for i in range(0, n2):
        r_arr[i] = arr[q + 1 + i]
    l_ind = 0
    r_ind = 0
    for i in range(left, right + 1):
        if l_ind < len(l_arr) and r_ind < len(r_arr):
            if l_arr[l_ind] <= r_arr[r_ind]:
                arr[i] = l_arr[l_ind]
                l_ind += 1
            else:
                arr[i] = r_arr[r_ind]
                r_ind += 1
        elif l_ind < len(l_arr):
            arr[i] = l_arr[l_ind]
            l_ind += 1
        else:
            arr[i] = r_arr[r_ind]
            r_ind += 1





