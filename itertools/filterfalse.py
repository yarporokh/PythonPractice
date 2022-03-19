import itertools

arr = [12, 3, 56, 33, 2, 8, 6, 44, 9, 0, 12]
f = itertools.filterfalse(lambda x: x < 10, arr)

print(list(f))

# Output: [12, 56, 33, 44, 12]
