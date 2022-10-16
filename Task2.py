'''Задача 2.
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 12, 123, 1234)'''

N = int(input("Введите число N: "))

set_of_multiplication = []
count = 1
for i in range(N):
    count *= i + 1
    set_of_multiplication.append(count)
print(f"Набор произведений числа N = {set_of_multiplication}")
