import itertools

c = itertools.cycle("QWER")

for i in range(12):
    print(next(c), end=" ")

# Output: Q W E R Q W E R Q W E R
