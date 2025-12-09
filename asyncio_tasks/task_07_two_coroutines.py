import asyncio
import aiohttp
from datetime import datetime


#Задание 7. Реализуйте асинхронный скрипт, который создает две корутины, выполняющие асинхронные операции, и выводит результаты.
async def coroutine_first():
    await asyncio.sleep(5)
    current_time = datetime.now().time()
    print(coroutine_first.__name__)
    print("Текущее время : ", current_time)


async def coroutine_second():
    await asyncio.sleep(2)
    current_time = datetime.now().time()
    print(coroutine_second.__name__)
    print("Текущее время : ", current_time)


async def delay_print(name, delay):
    await asyncio.sleep(delay)
    current_time = datetime.now().time()
    print(name)
    print("Текущее время : ", current_time)


async def main():
    ##7
    # await asyncio.gather(coroutine_first(), coroutine_second())
    await asyncio.gather(delay_print(name="coroutine_first", delay=5), delay_print(name="coroutine_second", delay=2))


asyncio.run(main())
