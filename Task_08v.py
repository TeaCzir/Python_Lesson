# Требуется определить, можно ли от шоколадки размером "b" × "a" долек отломить "c" долек, если
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника). 3 2 4 -> yes 3 2 1 -> no

a = int(input('Введите число долек стороны "b": '))
b = int(input('Введите число долек стороны "a": '))
c = int(input('Введите число долек "c": '))

print('Вы ввели: ', b, a, c)

if c <= b * a and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')