# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника). 3 2 4 -> yes 3 2 1 -> no

n = int(input('Введите число долек стороны "n": '))
m = int(input('Введите число долек стороны "m": '))
k = int(input('Введите число долек "k": '))

print('Вы ввели: ', n, m, k)

if m > n or n > m:
   if k == n or k == m or k % n == 0 or k % m == 0:
         print('yes')
   else:
         print('no')