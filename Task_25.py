# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

line = "a a a b c a a d c d d".split()
print(line)
res = {}

# for letter in line:
#     if letter not in res:
#         print(letter, end=' ')
#         res[letter] = 0
#     else:
#         res[letter] += 1
#         print(f"{letter}_{res[letter]}", end=' ')

#2
for letter in line:
    if letter not in res:
        print(letter, end=' ')        
    else:
        print(f"{letter}_{res[letter]}", end=' ')
    res[letter] = res.get(letter, 0) + 1