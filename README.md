Описание задания
1) Реализовать программу на вход которой подается список разных числе например [1, 4, 2, 4, 5, 7 ] . Необходимо узнать какие из элементов встречаются чаще всего - это может быть как одни элемент в случае [1, 4, 2, 2, 3] - это будет 2, либо несколько элементов если они встречаются одинаковое количество раз - [1, 2, 3, 4, 2, 4, 5] - тут ответ 2 и 4

2) созадть программу - базу данных, которая запрашивает у пользователей набор данных например название, количество и стоимость товара и сохраняют в какую-либо структуру (подобрать самостоятельно списки, словари тд). Реализовать меню в программе, которое состоит из следующих пунктов:
1) ввести данные
2) вывести все введенные ранее данные
3) выход

*2 - самая простоя задача, которую мне давали при собесе в Яндекс.
есть список состоящий из элементов 0 и 1. Например [0, 0, 0, 1, 0, 1] он может быть любой величины и содержать любой количество нулей и единиц. Представьте что этот список моделирует ряд в кинотеатре где 0 - место не занято, 1 - место занято. Необходимо найти номер незанятого сидения (индекс элемента) при посадке на которое мы будем максимально удалены от других сидящих посетителей.

Требования по памяти: O(1) - количество занимаемой дополнительными переменными памяти не изменяется в зависимости от размера переданного списка

Требования по алгоритмической сложности - O(n) - один проход по списку
