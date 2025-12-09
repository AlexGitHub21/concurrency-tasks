import asyncio
import aiohttp


#Задание 9. Разработайте асинхронный скрипт, который параллельно обрабатывает данные из двух разных источников
# и объединяет их в один результат.

async def get_joke(session, url):
    async with session.get(url) as response:
        return await response.json()


async def get_random_user(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    ##9
    async with aiohttp.ClientSession() as session:
        joke = asyncio.create_task(get_joke(session, "https://official-joke-api.appspot.com/random_joke"))
        random_user = asyncio.create_task(get_random_user(session, "https://randomuser.me/api/"))

        result_1, result_2 = await asyncio.gather(joke, random_user)
        print(
            f"Для рандомного пользователя по имени: {result_2['results'][0]['name']['first']} {result_2['results'][0]['name']['last']} "
            f"есть шутка: {result_1['setup']} {result_1['punchline']}")


asyncio.run(main())