from multiprocessing import Process, current_process
import os


def increment(num):
    res = num + 1
    print(f"{num} -> {res}, process ID: {os.getpid()}, name {current_process().name}")


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    procs = []
    for num in nums:
        p = Process(target=increment, args=(num,))
        procs.append(p)
        p.start()

    for proc in procs:
        proc.join()
