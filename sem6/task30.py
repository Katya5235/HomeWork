# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Input n ')) 
x = int(input('Input a[0] '))
d = int(input('Input d ')) 
print(*range(x, x + d * n, d))
