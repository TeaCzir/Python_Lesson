# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них
# новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом
# из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку) Output: 32


class_1 = int(input('Enter the number of students in the 1st grade: '))
class_2 = int(input('Enter the number of students in the 2st grade: '))
class_3 = int(input('Enter the number of students in the 3st grade: '))

tables_1 = ((class_1 + 1) // 2)
tables_2 = ((class_2 + 1) // 2)
tables_3 = ((class_3 + 1) // 2)

print(tables_1 + tables_2 + tables_3)

