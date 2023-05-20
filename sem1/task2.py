# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
print (' Введите число: ')
n = int (input())
sum_of_digits = 0

while n > 0:
    digit = n % 10
    n = n // 10
    sum_of_digits = sum_of_digits + digit 

print (sum_of_digits) 



