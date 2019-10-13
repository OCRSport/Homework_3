new_list = []
n = int(input('Введите количество элементов: '))
for i in range(n):
    print('Введите', i + 1, 'элемент: ')
    new_el = int(input())
    new_list.append(new_el)
    new_list.sort()
print(new_list)
