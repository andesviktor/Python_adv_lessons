from threading import Event, Semaphore, Lock, RLock
import time, random
from queue import Queue


class Pipeline(Queue):
    def __init__(self):
        super(Pipeline, self).__init__(maxsize=10)

    def get_msg(self):
        value = self.get()
        return value

    def set_msg(self, value):
        self.put(value)


def producer(pipeline, event):
    while not event.is_set():
        msg = random.randint(1, 101)
        print(f'producer got msg: {msg}')
        pipeline.set_msg(msg)

    print(f'Producer "is set" finish working. Finish!')


def consumer(pipeline, event):
    while not event.is_set() or not pipeline.empty():
        msg = pipeline.get_msg()
        print(f'consumer got msg: {msg}')

    print(f'Consumer "is set" finish working. Finish!')


if __name__ == "__main__":
    pipeline = Pipeline()
    event = Event()
    with ThreadPoolExecutor(max_workers=2) as ex:
        ex.submit(producer, pipeline)
        ex.submit(consumer, pipeline)

        print('Main thread say: Start!')
        time.sleep(0.1)
        event.set()
