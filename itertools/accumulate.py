import itertools

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = itertools.accumulate(arr)

print(list(a))

# Output: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
