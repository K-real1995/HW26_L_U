# 2) созадть программу - базу данных, которая запрашивает у пользователей набор данных например название, количество
# и стоимость товара и сохраняют в какую-либо структуру (подобрать самостоятельно списки, словари тд).
# Реализовать меню в программе, которое состоит из следующих пунктов:
#
# 1) ввести данные
# 2) вывести все введенные ранее данные
# 3) выход
import json
from pathlib import Path


def get_data_in_db():
    with open('base.json') as f:
        data = json.load(f)
        return data["products"] if data["products"] else None


def make_data_in_db(title, quantity, cost):
    path = Path('base.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    # Data to be written
    dictionary = {
        "Название": title,
        "Количество": quantity,
        "Цена": cost
    }

    data['products'].append(dictionary)

    # Serializing json
    path.write_text(json.dumps(data), encoding='utf-8')


while True:
    choice = int(input("___Меню___\n"
                       "1.Ввести данные\n"
                       "2 Вывести все введенные ранее данные\n"
                       "3.Выход\n"))
    if choice == 1:
        name = input("Введите название: ")
        count = int(input("Введите количество: "))
        price = int(input("Введите цену: "))
        make_data_in_db(name, count, price)
        print("Данные успешно добавлены")
    elif choice == 2:
        print(get_data_in_db())
    elif choice == 3:
        print("Выходим из программы")
        break  # Выход из цикла программы
