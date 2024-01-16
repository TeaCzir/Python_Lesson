# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

size = int(input("Enter size: "))
x = int(input("Enter x: "))

list_1 = [randint(1, 40) for i in range(size)]
print(list_1)

m = abs(x - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - x):
        m = abs(list_1[i] - x)
        number = list_1[i]
print(number)