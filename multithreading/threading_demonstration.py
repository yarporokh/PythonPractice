import threading
import os


def task1():
    print(f"Task 1 thread name: {threading.current_thread().name}")
    print(f"ID of task 1 process: {os.getpid()}")


def task2():
    print(f"Task 2 thread name: {threading.current_thread().name}")
    print(f"ID of task 2 process: {os.getpid()}")


print(f"Main task thread name: {threading.current_thread().name}")
print(f"ID of main process: {os.getpid()}")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2, name="TASK-2-THREAD")
t1.start()
t2.start()

t1.join()
t2.join()

# Expected output:
#
# Main task thread name: MainThread
# ID of main process: 13660
# Task 1 thread name: Thread-1
# ID of task 1 process: 13660
# Task 2 thread name: TASK-2-THREAD
# ID of task 2 process: 13660
