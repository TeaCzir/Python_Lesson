# Задача №39.  1) Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком 
# они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов 
# в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. 
# Затем элементы второго массива.
# 2) (пользовательский ввод можно заменить на рандомный ввод)
# Пользователь вводит  размер первого массива – N
# и элементы первого массива. 
# затем размер второго массива M  
# и элементы второго массива
# Нужно вывести те элементы первого массива, которых нет во втором массиве, при этом порядок последовательности 
#сохранить исходный
# Ввод: 			Вывод:
# 7			3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1


from random import randint

size_1 = int(input("Enter array size: "))
# list_1 = list()
# for _ in range(size_1):
#     list_1.append(randint(1, 10))

list_1 = [randint(1, 10) for _ in range(size_1)]
print(list_1)

size_2 = int(input("Enter array size: "))
# list_2 = list()
# for _ in range(size_2):
#     list_2.append(randint(1, 10))

list_2 = [randint(1, 10) for _ in range(size_2)]
print(list_2)

for num in list_1:
    if num not in list_2:
        print(num, end = ' ')