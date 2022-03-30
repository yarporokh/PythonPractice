def lin_search(arr, n):
    for i in range(len(arr) - 1):
        if n == arr[i]:
            return i

    return


arr = [34, 12, 41, 53, 24, 66, 14, 64]
n = 41
k = 99
print(f"ID of {n} = {lin_search(arr, n)}")
print(f"ID of {k} = {lin_search(arr, k)}")

# Expected output:
#
# ID of 41 = 2
# ID of 99 = None
