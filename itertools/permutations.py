import itertools

p1 = itertools.permutations("QWER", 2)

for i in list(p1):
    print(i)

p2 = itertools.permutations("QWER", 3)

for i in list(p2):
    print(i)

