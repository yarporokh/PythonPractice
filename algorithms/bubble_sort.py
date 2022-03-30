def b_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [3, 51, 87, 15, 23, 45, 88, 32, 15]
b_sort(arr)

print(arr)  # Output: [3, 15, 15, 23, 32, 45, 51, 87, 88]
