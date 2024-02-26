import asyncio
from time import perf_counter

async def fn():
	time_before = perf_counter()
	print('This is ')
	await asyncio.sleep(1)
	print('asynchronous programming')
	await asyncio.sleep(1)
	print('and not multi-threading')
    total_time = perf_counter() - time_before
    print(f"Total time taken to run the program {total_time}")

asyncio.run(fn())
