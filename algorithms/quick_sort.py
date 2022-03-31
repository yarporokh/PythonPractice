def q_sort(arr, low, high):
    if len(arr) == 0:
        return

    if low >= high:
        return arr

    mid = low + (high - low) // 2
    opora = arr[mid]

    i, j = low, high

    while i <= j:
        while arr[i] < opora:
            i += 1
        while arr[j] > opora:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    if low < j:
        q_sort(arr, low, j)
    if high > i:
        q_sort(arr, i, high)


arr = [4, 12, 59, 34, 12, 93, 28, 14, 0, 64, 22, 67, 75, 12, 54]
low = 0
high = len(arr) - 1
q_sort(arr, low, high)
print(arr)  # Output: [0, 4, 12, 12, 12, 14, 22, 28, 34, 54, 59, 64, 67, 75, 93]
