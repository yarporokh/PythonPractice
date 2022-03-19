import itertools

c = 0
nums = itertools.count(0, 7)
for n in nums:
    if c == 20:
        break
    c += 1
    print(n, end=' ')

# Output: 0 7 14 21 28 35 42 49 56 63 70 77 84 91 98 105 112 119 126 133
