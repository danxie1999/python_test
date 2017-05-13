import aiohttp,asyncio

async def print_page(url):
	response=await aiohttp.request('GET',url)
#	print(response)
	print(type(response))
#	body=await response.read(decode=True)
#	print(body)

loop = asyncio.get_event_loop()

loop.run_until_complete(print_page('https://www.python.org/'))