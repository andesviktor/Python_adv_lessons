from time import time
import urllib.request
import asyncio, aiohttp

url = 'https://api.github.com/events'

async def read_events(session, num):
    print(f'Task #{num} started')
    start = time()
    async with session.get(url) as resp:
        datetime = resp.headers.get('Date')

    print(f'Task #{num}: {datetime} took {time() - start} sec.')
    return datetime


async def async_func_start():
    start = time()
    async with aiohttp.ClientSession as sess:
        tasks = [asyncio.ensure_future(read_events(sess,i)) for i in range(3)]
        await asyncio.wait(tasks)
    print(f'Time {time() - start} sec.')

loop = asyncio.get_event_loop()
loop.run_until_complete(async_func_start())