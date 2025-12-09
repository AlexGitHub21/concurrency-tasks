import asyncio
import aiohttp


#Задание 10. Напишите асинхронный скрипт для выполнения двух асинхронных операций с использованием asyncio.gather()
# и выводите результаты.
async def operation_first():
    await asyncio.sleep(6)
    print(operation_first.__name__)


async def operation_second():
    await asyncio.sleep(2)
    print(operation_second.__name__)


async def main():
    # 10
    await asyncio.gather(operation_first(), operation_second())


asyncio.run(main())