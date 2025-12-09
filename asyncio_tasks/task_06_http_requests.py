import asyncio
import aiohttp


#Задание 6. Напишите программу, которая асинхронно отправляет два HTTP-запроса на разные серверы и выводит результаты.
async def fetch_get(session, url):
    async with session.get(url) as response:
        return await response.json()


async def main():
    ##6
    async with aiohttp.ClientSession() as session:
        name = "Vadim"
        country = "Kazakhstan"
        fetch_one = asyncio.create_task(fetch_get(session, f"https://api.agify.io/?name={name}"))
        fetch_two = asyncio.create_task(fetch_get(session, f"http://universities.hipolabs.com/search?country={country}"))

        result1, result2 = await asyncio.gather(fetch_one, fetch_two)

        print(f"Рандомный пользователь по имени {name}: {result1}")
        print(f"Список университетов страны {country}: ")
        for univ in result2:
            print("-", univ["name"])



asyncio.run(main())