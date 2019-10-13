elements = input('Введите элементы списка через запятую: ')
new_list = list(int(i) for i in elements.replace(';', ',').replace('/', ',').split(','))
print(new_list)
new_set = set(new_list)
print(new_set)

