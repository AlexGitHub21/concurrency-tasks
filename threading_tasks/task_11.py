import threading

#Задание 11. Напишите программу, которая создает два потока для выполнения двух задач параллельно:
# один поток печатает числа от 1 до 5, а другой поток печатает их квадраты

def print_number():
    for i in range(1,6):
        print(f"Number: {i}")

def print_squares_number():
    for i in range(1,6):
        print(f"Square: {i**2}")

thread_1 = threading.Thread(target=print_number, name="numbersThread")
thread_2 = threading.Thread(target=print_squares_number, name="squares_numberThread")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()