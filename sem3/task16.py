# Задача 16: Требуется вычислить, сколько раз встречается некоторое число 
# X в списке A. Пользователь в первой строке вводит натуральное число N – количество
# элементов  в массиве.

# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите количество элементов в массиве: '))
list_a = input('Введите элементы массива через пробел: ').split()
arr = list(map(int, list_a))
if len(arr) != n:
    print('Колличество элементов не верно!')
else:
    x = int (input('Введите искомое число: '))
    sum = 0
    for i in range(n):
        if arr[i] == x:
            sum += 1
    print(f'Число {x} встречается в массиве {sum} раз(а).')