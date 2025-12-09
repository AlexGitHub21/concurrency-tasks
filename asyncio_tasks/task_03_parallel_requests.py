import asyncio
import aiohttp


#Задание 3. Создайте асинхронный веб-сервер, который обрабатывает запросы на два различных URL параллельно.
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    ##3
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(fetch(session, "https://jsonplaceholder.typicode.com/posts/1"),
                                       fetch(session, "https://jsonplaceholder.typicode.com/posts/2"))
        print(results[0])
        print(results[1])

asyncio.run(main())