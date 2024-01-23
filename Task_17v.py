# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел. 
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
from random import randint
size = int(input("Enter size: "))

list1 = []
for _ in range(size):
    num = randint(1, 10)
    list1.append(num)
# list1 = [randint(1, 10) for _ in range(size)]

print(list1)
print(len(set(list1)))
