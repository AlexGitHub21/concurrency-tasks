#Задание 15. Создайте программу, в которой три потока выполняют различные вычислительные задачи,
# а главный поток ожидает их завершения и выводит результаты.
import random
import threading
from queue import Queue


def sum_a_and_b(a, b):
    result.put(("Сумма a и b", a + b))

def generate_random_num():
    random_nums = [random.randint(1,50) for _ in range(5)]
    result.put(("Случайные числа", random_nums))

def minus_a_and_b(a, b):
    if a > b:
        result.put(("Разность a и b", a / b))
    else:
        result.put(("Разность a и b", b / a))


if __name__ == '__main__':
    result = Queue()

    thread_1 = threading.Thread(target=sum_a_and_b, args=(1, 2))
    thread_2 = threading.Thread(target=minus_a_and_b, args=(1, 2))
    thread_3 = threading.Thread(target=generate_random_num)

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()

    for _ in range(3):
        name, value = result.get()
        print(f"{name}: {value}")
