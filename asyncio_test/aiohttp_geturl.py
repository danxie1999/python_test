#import asyncio,time,random,datetime,subprocess,aiohttp

import aiohttp
import asyncio
import async_timeout


#loop = asyncio.get_event_loop()
#loop.run_until_complete(main(loop))
async def print_page(url):
	with async_timeout.timeout(10):
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as resp:
				print(resp.status)
				print(await resp.text())

async def fetch(session,url):
	with async_timeout.timeout(10):
		async with session.get(url) as res:
			return await res.status
async def main(loop):
	async with aiohttp.ClientSession(loop) as session:
		html= await fetch(session,'http://python.org')
		print(html)

loop=asyncio.get_event_loop()
tasks=[print_page('http://163.com'),print_page('http://google.com')]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
