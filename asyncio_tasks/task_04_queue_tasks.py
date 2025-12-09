import asyncio
import aiohttp
from datetime import datetime


#Задание 4. Напишите программу, которая создает очередь из 5 асинхронных задач и выполняет их параллельно.
# Задачи должны печатать свой номер и текущее время.
async def print_task(num):
    await asyncio.sleep(num)
    current_time = datetime.now().time()
    print("Номер задачи: ", num)
    print("Текущее время: ", current_time)


async def main():
    ##4
    tasks = [asyncio.create_task(print_task(num=i)) for i in range(1, 6)]
    await asyncio.gather(*tasks)


asyncio.run(main())
