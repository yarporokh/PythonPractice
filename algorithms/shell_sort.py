def s_sort(arr):
    n = len(arr)
    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i

            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp

        interval //= 2


arr = [43, 22, 1, 54, 98, 76, 53, 76, 6, 0, 66, 33]
s_sort(arr)
print(arr)  # Output: [0, 1, 6, 22, 33, 43, 53, 54, 66, 76, 76, 98]
