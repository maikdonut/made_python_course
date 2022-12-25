import asyncio
import time
import sys
import aiohttp


async def fetch_url(url, session):
    async with session.get(url) as resp:
        data = await resp.read()
        return len(data)


async def worker(queue, session, i):
    while True:
        url = await queue.get()
        res = await fetch_url(url, session)
        print(
            "============================\n",
            f"worker-{i + 1} has done his deal",
            "\n",
            "len(data) = ",
            res,
            sep="",
        )


async def main():
    queue = asyncio.Queue()
    for line in open(file_name):
        await queue.put(line.strip())

    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(worker(queue, session, i)) for i in range(workers)]
        started_at = time.monotonic()
        await queue.join()
        total_sleep_time = time.monotonic() - started_at
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    workers = 10
    file_name = "urls.txt"
    for param in sys.argv:
        if param.isdigit():
            workers = int(param)
        elif ".txt" in param:
            file_name = param
    asyncio.run(main())
