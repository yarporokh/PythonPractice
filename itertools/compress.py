import itertools

symbols = "ASHGAELLETOWGFORDPPLDP"
selectors = [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0]

c = itertools.compress(symbols, selectors)
print("".join(list(c)))

# Output: HELLOWORLD
