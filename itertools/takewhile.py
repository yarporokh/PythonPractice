import itertools

p = itertools.takewhile(lambda x: x < 5, [2, 1, 4, 6, 3, 2, 7])

for i in list(p):
    print(i, end=" ")

# Output: 2 1 4
