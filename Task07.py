# Задача №7 Дано натуральное число - год. Требуется определить, является ли год с данным
# номером високосным. Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным,
# (если его номер кратен 4, но не кратен 100), а также если он кратен 400.
# Input: 2016
# Output: YES

year = int(input("Введите номер года: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Yes")
else:
    print("No")



