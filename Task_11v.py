# Дано натуральное число А > 1. Определите, каким по счету числом Фибоначи оно является, то есть
# выведите такое число n, ч ϕ(n) = А. Если А не является числом Фибоначи, выведите число -1.
# Input: 5    Output: 6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 
 
a = int(input('Введите число Фибоначи: '))

n1 = 1
n2 = 2

count = 4

while n2 < a:
     n2, n1 = n1 + n2, n2
     count += 1

if n2 != a: 
    count = -1   
print(count)