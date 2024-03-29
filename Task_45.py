# Задача №45.  Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно 
# натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в 
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# (пользовательский ввод можно заменить на рандомный)
# Пользователь вводит  натуральное число  – k
# В диапазоне от 0 до k нужно вывести все пары чисел N и M, в которых сумма делителей N равняется M, а сумма делителей M равняется N (число само на себя делить нельзя)
# Пары необходимо выводить по одной паре в строке, разделяя числа пробелами. Каждая пара выводится только один раз, без повторов.
# Пример: Возьмём 2 числа 220 и 284. Найдём их делители 
# Делители 220 – (1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110)
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110  = 284
# Делители 284 – (1, 2, 4, 71, 142 )
# 1 + 2 + 4 + 71 + 142 = 220
# 			Ввод:			Вывод:
# 			300			220 284


import math

def div_sum(number):
    sum_div = 1
    sqrt_num = number ** 0.5
    if sqrt_num == int(sqrt_num):
        sum_div += int(sqrt_num)
    for div in range(2, int(sqrt_num)):
        if number % div == 0:
            sum_div += div + (number // div)
    return sum_div
    

k = int(input('Введите число k: '))

for num_1 in range(2, k):
    num_2 = div_sum(num_1)
    if div_sum(num_2) == num_1 and num_1 < num_2:
        print(num_1, num_2)