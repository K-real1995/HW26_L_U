# Функция для случайной генерации ряда в кинотеатре

from random import randint

length = randint(0, 50)
lst = [randint(0, 1) for _ in range(length)]
print(lst)
