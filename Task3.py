'''Задача 3.
Реализуйте алгоритм перемешивания списка. 
Список размерностью 10 задается случайными целыми числами, 
выводится на экран, затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!'''

from random import randint

n = int(input("Введите количество элементов списка: "))
random_list = [randint(0, 20) for i in range(n)]
print(random_list)
for i in range(n):
    temp = random_list[i]
    j = randint(0, n - 1)
    random_list[i] = random_list[j]
    random_list[j] = temp
print(random_list)
