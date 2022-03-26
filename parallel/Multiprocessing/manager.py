from multiprocessing import Process, Manager

def func(v, d, l, q):
    v.value = 3.14
    d['Name'] = 'Bob'
    l.append(20)
    q.put(['John', 12, None])

if __name__ == '__main__':
    manager = Manager()
    v = manager.Value('d', 0.0)
    d = manager.dict()
    l = manager.list()
    q = manager.Queue()
    p = Process(target=func, args=(v, d, l, q))

    p.start()
    p.join()

    print(v.value)
    print(d)
    print(l)
    print(q.get())

# Expected output:
#
# 3.14
# {'Name': 'Bob'}
# [20]
# ['John', 12, None]
