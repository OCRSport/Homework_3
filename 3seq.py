elements_1 = input('Введите элементы списка №1: ')
list_1 = list(int(i) for i in elements_1.replace(';', ',').replace('/', ',').split(','))
set_1 = set(list_1)
elements_2 = input('Введите элементы списка №2: ')
list_2 = list(int(i) for i in elements_2.replace(';', ',').replace('/', ',').split(','))
set_2 = set(list_2)
result = set(list_1) - set(list_2)
print(result)