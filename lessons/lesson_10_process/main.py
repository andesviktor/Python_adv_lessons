from multiprocessing import Process


def func():
    print('Hello from child Process')


if __name__ == "__main__":
    proc = Process(target=func)
    proc.start()
