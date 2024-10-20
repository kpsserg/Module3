def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print("передадим в ф-ю разные параметры")
print_params()
print_params(b = 25)
print_params(c = False)

print("\nПередадим в ф-ю список")
values_list = [('a', 'b', True), [4, 5], {1, 2}]
print_params(values_list)
print_params(*values_list)

print("\nПередадим в ф-ю словарь")
values_dict = { 'a': "Serg", 'b': 42, 'c': 1981}
print('Без распаковки:')
print_params(values_dict)
print('С распаковкой параметров словаря:')
print_params(**values_dict)

values_list = [5]
values_dict = {'b' : 'Student', 'c' : 'Python'}
print(f"\nПередадим в ф-ю распакованные "
      f"\nи список {values_list}, "
      f"\nи словарь {values_dict}:")
print_params(*values_list, **values_dict)


values_list_2 = [54.32, 'Строка' ]
print(f'\nпередадим в ф-ю одновременно: \n1) распакованный список из двух элементов {values_list_2} \n2) и ещё один параметр')
print_params(*values_list_2, 42)
