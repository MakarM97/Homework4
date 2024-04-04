immutable_var = 1, 2.2, True, 'String'
print(immutable_var)
#immutable_var [0] = 4 #Кортеж является неизменяемым объектом, соответвенно ошибка
mutable_list = ([1, 2, 'apple'], 55)
mutable_list[0][0] = False
print(mutable_list)