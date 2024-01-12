# 1) Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для 
# себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же 
# выбрать самый легкий и самый тяжелый арбуз? Помогите ему! Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего 
# арбуза 2) Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое. 
# Вывести максимальное и минимальное (циклы) Input:	5 -> 5 1 6 5 9   Output:	1 9


from random import randint

watermelon = int(input("Enter watermelon amount: "))
weight = randint(1, 10)
print(weight, end = ' ')
min_weight = weight
max_weight = weight

for _ in range(watermelon - 1):
    weight = randint(1, 10)
    print(weight, end = ' ')
    max_weight = max(weight, max_weight)
    min_weight = min(weight, min_weight)
    
print()
print(min_weight, max_weight)