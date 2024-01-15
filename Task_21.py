# Задача №21. Напишите программу для печати всех уникальных значений в словаре.

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dicts = [{"VII": "S055","V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

#1 
# unique = set()                             # list dictionary - список словарей. unique - уникалный.
# for curr_dict in list_dicts:               # current dictionary - текущий словарь. 
#     for value in curr_dict.values():       #  value - значение (ценность.)
#         unique.add(value)
# print(unique)

#2
# unique = set()
# for curr_dict in list_dicts:
#     # print(*curr_dict.values()) 
#     unique.add(*curr_dict.values())      
# print(unique) 

#3
unique = set()
for curr_dict in list_dicts:
    unique.update(curr_dict.values())      
print(unique)