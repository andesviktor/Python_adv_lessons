import concurrent.futures
import threading
from random import randint
import time
from itertools import count, islice
from math import sqrt

from multiprocessing import Process, Queue, Event

n = 0


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def producer(queue: Queue, event):
    i = 0
    while not event.is_set():
        i += 1
        if not is_prime(i):
            continue
        queue.put(i)
    print('finish producer')


def consumer(queue: Queue, event):
    global n
    while not event.is_set() or not queue.empty():
        msg = queue.get()
        n += 1
        print(f'{n}) {msg} - {is_prime(msg)}')


if __name__ == '__main__':
    pipeline = Queue(maxsize=10)
    event = Event()

    p_p = Process(target=producer,args=(pipeline,event,), daemon= True)
    p_p.start()
    p_c = Process(target=consumer, args=(pipeline, event,), daemon=True)
    p_c.start()
    # with concurrent.futures.ProcessPoolExecutor(max_workers=2) as ex:
    #     ex.submit(producer, pipeline, event)
    #     ex.submit(consumer, pipeline, event)
    while not p_c.is_alive():
        pass