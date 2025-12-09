import asyncio
import aiohttp


#Задание 2. Реализуйте функцию, которая асинхронно скачивает две картинки из сети параллельно и сохраняет их на диск
async def download_image(session, url, filename):
    print("Начало загрузки: ", filename)
    async with session.get(url) as response:
        data = await response.read()
        with open(filename, "wb") as f:
            f.write(data)
    print("Скачано: ", filename)


async def main():
    ##2
    async with aiohttp.ClientSession() as session:
        task_three = asyncio.create_task(download_image(session, url="https://cdn.pixabay.com/photo/2025/10/26/13/00/ai-generated-9917901_1280.png", filename="bird.png"))
        task_four = asyncio.create_task(download_image(session, url="https://cdn.pixabay.com/photo/2024/03/30/15/51/cat-8664948_1280.jpg", filename="cat.jpg"))

        await asyncio.gather(task_three, task_four)

asyncio.run(main())