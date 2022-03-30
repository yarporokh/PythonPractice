def m_sort(arr):
    if len(arr) == 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    m_sort(left)
    m_sort(right)

    i = j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


array = [43, 12, 48, 22, 89, 67, 53, 12, 0, 9, 74]
m_sort(array)
print(array) # Output: [0, 9, 12, 12, 22, 43, 48, 53, 67, 74, 89]

