import requests
from concurrent.futures import ThreadPoolExecutor
#for requests_futures import sessions
#import asyncio
#import aiohttp

################################################
#Note: VAR 1
################################################
# session = requests.Session()
# session.get('http://google.com')
# #re-used
# session.get('http://google.com')
################################################

################################################
#Note: VAR 2
################################################
# with ThreadPoolExecutor() as ex:
#     futures = [
#         ex.submit(lambda:requests.get('http://google.com'))
#         for _ in range(10)
#     ]
#
# results = [f.result().status_code for f in futures]
# print(f'Res: {results}')
################################################
################################################
# Note: VAR 3
################################################
# sessions = sessions.FuturesSessioin(executor=ThreadPoolExecutor(max_workers=12))
#
# futures = [
#     sessions.get('http:google.com')
#     for _ in range(10)
# ]
# results = [f.results().status_code for f in futures]
# print(f'Res: {results}')
################################################
################################################
# Note: VAR 4
################################################

# async def get(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as resp:
#             return resp.status
#
# loop = asyncio.get_event_loop()
# cors = [get('http://google.com') for _ in range(10)]
# res = loop.run_until_complete(asyncio.gather(*cors))
# print(f'Res: {res}')
################################################

from contextlib import contextmanager
from time import time
import asyncio
import aiohttp
import requests
from request_futures import sessions

URl = 'http://httpbin.org/delay/1'
N_COUNT = 10

def el_time(test):
    start = time()
    yield
    print(f'Time for {test} need: {time() - start}')

with el_time('simple'):
    for _ in range(N_COUNT):
        requests.get(URl)