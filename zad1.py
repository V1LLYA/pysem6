# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
# n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = float(input("Введите первый элемент прогрессии (a1): "))
d = float(input("Введите разность прогрессии (d): "))
n = int(input("Введите количество элементов в прогрессии (n): "))
for i in range(n):
    print(a1 + i * d, end=' ')