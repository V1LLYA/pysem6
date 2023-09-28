# Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

lst = [random.randint(-100, 200) for _ in range(10)]

min_value = 33
max_value = 200

indices = []

for i, value in enumerate(lst):
    if min_value <= value <= max_value:
        indices.append(i)

print("Исходный список:", lst)
print("Минимум:", min_value)
print("Максимум:", max_value)
print("Индексы элементов в заданном диапазоне:", indices)
