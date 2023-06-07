# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

prime_number = int(input("Введите число: "))
counter = 0
for i in range (2, prime_number // 2+1):
    if (prime_number % i == 0 ):
        counter = counter +1 

if (counter <= 0 ):
    print ("Число простое! ")
else:
    print("Число непростое! ")     
