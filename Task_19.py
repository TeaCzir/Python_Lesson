# Задача №19.  Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

# Input:   [1, 2, 3, 4, 5] k = 3

# Output:  [3, 4, 5, 1, 2]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = 4

# for i in range(k):
#     last_num = numbers.pop()
#     numbers.insert(0, last_num)
# print(f'{numbers=}')

print(f'{numbers[-k:] + numbers[:-k] = }')