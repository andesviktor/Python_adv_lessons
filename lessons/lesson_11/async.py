import asyncio
from time import time

start = time()
def tic():
    return f'time: {time() - start}'

async def task_1():
    print(f'Task #1 starting. time: {tic()}')
    await asyncio.sleep(1)
    print(f'Task #1 finishing. time: {tic()}')

async def task_2():
    print(f'Task #2 starting. time: {tic()}')
    await asyncio.sleep(2)
    print(f'Task #2 finishing. time: {tic()}')

async def task_3():
    print(f'Task #3 starting. time: {tic()}')
    await asyncio.sleep(5)
    print(f'Task #3 finishing. time: {tic()}')

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(task_1()),
    loop.create_task(task_2()),
    loop.create_task(task_3())
]
wait_tasks = asyncio.wait(tasks)
loop.run_until_complete(wait_tasks)