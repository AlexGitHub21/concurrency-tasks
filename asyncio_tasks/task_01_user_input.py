import asyncio

#Задание 1. Напишите программу, которая ожидает получения числа от пользователя b
# и параллельно запускает две задачи печати числа b через 3 секунды.


async def second_print_num_user(b):
    await asyncio.sleep(3)
    print(f"Число введенное пользователем 2: {b}")


async def first_print_num_user(b):
    await asyncio.sleep(3)
    print(f"Число введенное пользователем 1: {b}")


async def main():
    ##1
    b = int(input("Укажите любое число: "))
    task_one = asyncio.create_task(first_print_num_user(b))
    task_two = asyncio.create_task(second_print_num_user(b))
    await asyncio.gather(task_one, task_two)

asyncio.run(main())