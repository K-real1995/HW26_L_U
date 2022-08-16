# 1) Реализовать программу на вход которой подается список разных чисел например [1, 4, 2, 4, 5, 7 ] . Необходимо узнать
# какие из элементов встречаются чаще всего - это может быть как одни элемент в случае [1, 4, 2, 2, 3] - это будет 2,
# либо несколько элементов если они встречаются одинаковое количество раз - [1, 2, 3, 4, 2, 4, 5] - тут ответ 2 и 4
from collections import Counter


def mode(x):
    if not x:  # Сразу проверяем, что исходный список не пустой
        return []
    else:
        most_common = Counter(x).most_common()
        max_count = most_common[0][1]
        result = []
        for x, count in most_common:
            if count < max_count:
                break
            else:
                result.append(x)
        return result
