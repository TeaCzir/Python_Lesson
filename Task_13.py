# Задача №13. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая 
# длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней 
# длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура 
# ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 10). В следующих 
# строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий 
# день. Температуры – целые числа и лежат в диапазоне от –50 до 50 Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

import random
 
days = int(input('Введите количество дней: '))
max_count = 0 # максимальное число идущих последовательно плюсовых температур.
counter = 0

for _ in range(days):
    t = random.randint(-50, 50)
    print(t, end = ' ')
    if t > 0:
        counter += 1
        if counter > max_count:
            max_count = counter
    else:
        counter = 0
print()
print(f'{max_count = }')                


