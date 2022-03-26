from multiprocessing import Process, Value, Array


def func(v, a):
    v.value = 1000
    for i in range(len(a)):
        a[i] = a[i] ** 2


if __name__ == '__main__':
    value = Value('d', 0.0)
    array = Array('i', range(10))

    p = Process(target=func, args=(value, array))
    p.start()
    p.join()

    print(value.value)
    print(array[:])
