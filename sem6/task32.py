# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [9, 20, -6, 33, 8, -42, -151, 964, -2, 110, 2, 0, -9, 8, 10, 89, 0, 14, 9, 7]
list_2 = []
max = 100
min = 36

for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')