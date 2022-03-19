import itertools

l = itertools.islice("QWERTYUIO", 2, None)

for i in l:
    print(i, end=" ")

# Output : E R T Y U I O


l2 = itertools.islice("QWERTYUIO", 2, None, 2)
print("\n")
for i in l2:
    print(i, end=" ")

# Output: E T U O
