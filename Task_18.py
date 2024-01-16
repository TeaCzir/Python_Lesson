# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

size = int(input("Enter size: "))
x = int(input("Enter x: "))

list_1 = [randint(1, 40) for i in range(size)]
print(list_1)
close = 0
y = x - list_1[0]
min = abs(y)
for i in range(1, size):
    c = x - list_1[i]
    buffer = abs(c)
    if buffer < min:
        min = buffer
        close = i

print(list_1[close])

