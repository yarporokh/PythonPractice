def bin_search(a):
    a.sort()
    high = len(a) - 1
    mid = len(a) // 2
    low = 0

    value = int(input("Enter a value: "))

    print(a)

    while high >= low and value != a[mid]:
        if value > a[mid]:
            low += 1
        else:
            high -= 1
        mid = (low + high) // 2

    if low > high:
        print("No value in array")
    else:
        print(f"Value position in array: {mid}")


arr = [1, 52, 31, 4, 23, 12, 3, 4, 65, 83, 43]
bin_search(arr)
