import asyncio
import json
from aiohttp import ClientSession
from time import time


async def get_json(client: ClientSession, url):
    async with client.get(url) as r:
        return await r.read()


async def get_reddit_top(subreddit, client):
    data = await get_json(client, 'https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')

    j = json.loads(data.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        print(str(score) + ': ' + title + '( ' + link + ')')

    print('DONE', subreddit + '\n')


subreddits = ['python', 'programming', 'games', 'crypto', 'sports', 'movies', 'XRP', ]


async def create_tasks():
    async with ClientSession() as session:
        tasks = [asyncio.ensure_future(get_reddit_top(subreddit, session)) for subreddit in subreddits]
        await asyncio.wait(tasks)


loop = asyncio.get_event_loop()
loop.run_until_complete(create_tasks())

############################
# THREADS
############################

# from concurrent.futures import ThreadPoolExecutor
# from time import time
# import requests
# import json
#
#
# def get_json(url):
#     start = time()
#     with requests.get(url) as r:
#         data = r.json
#
#     print(f'took {time() - start} sec')
#     return data
#
#
# def get_reddit_top(subreddit):
#     data = get_json('https://www.reddit.com/r/' + subreddit + '/top.json?sort=top&t=day&limit=5')
#
#     for i in data['data']['children']:
#         score = i['data']['score']
#         title = i['data']['title']
#         link = i['data']['url']
#         print(str(score) + ': ' + title + '( ' + link + ')')
#
#     print('DONE', subreddit + '\n')
#
#
# subreddits = ['python', 'programming', 'games']
#
# with ThreadPoolExecutor() as ex:
#     ex.map(get_reddit_top, subreddits)
