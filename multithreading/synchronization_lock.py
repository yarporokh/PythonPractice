import threading

l = list()


def add_one():
    global l
    l.append(1)


def task(lock):
    for _ in range(5):
        lock.acquire()
        add_one()
        lock.release()


def main():
    global l
    l = list()
    lock = threading.Lock()

    t1 = threading.Thread(target=task, args=(lock,))
    t2 = threading.Thread(target=task, args=(lock,))
    t3 = threading.Thread(target=task, args=(lock,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


for i in range(5):
    main()
    print(f"Operation {i + 1}, result {l}")


# Expected output:
#
# Operation 1, result [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Operation 2, result [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Operation 3, result [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Operation 4, result [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Operation 5, result [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
