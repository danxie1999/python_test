import asyncio,time,random,datetime,subprocess,threading

#@asyncio.coroutine

async def wget(host):
	print("wget {}...".format(host))
	connect=asyncio.open_connection(host,80)
	reader,writer = await connect
	header='GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
	writer.write(header.encode('utf-8'))

	await writer.drain()
	while True:
		line= await reader.readline()
		if line == b'\r\n':
			break
		await asyncio.sleep(1)
		print("{}:{} header > {}".format(datetime.datetime.now(),host,line.decode('utf-8').strip()))

	writer.close()

loop = asyncio.get_event_loop()

tasks = [wget(host) for host in ['www.sina.com.cn','www.163.com.cn','www.shouhu.com']]
#tasks=[test()]

loop.run_until_complete(asyncio.wait(tasks))
#loop.run_until_complete(test())

loop.close()
