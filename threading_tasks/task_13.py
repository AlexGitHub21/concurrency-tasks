#Задание 13. Напишите программу, в которой создается поток для генерации случайных чисел и поток для вычисления
# их среднего значения. Используйте механизм синхронизации для безопасного доступа к общим данным.

import random
import threading
from queue import Queue

count_nums = 10
queue = Queue()

def generate_random_num():

    random_nums = [random.randint(1, 100) for _ in range(count_nums)]
    queue.put(random_nums)

def calculate_average():

    random_nums = queue.get()
    average = sum(random_nums) / len(random_nums)
    print(f"Среднее значение 10 сгенерированных чисел: {average}")
    queue.task_done()


thread_generate_random_num = threading.Thread(target=generate_random_num)
tread_calculate_average = threading.Thread(target=calculate_average)

thread_generate_random_num.start()
tread_calculate_average.start()

thread_generate_random_num.join()
tread_calculate_average.join()


