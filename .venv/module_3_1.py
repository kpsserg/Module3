#Функция count_calls подсчитывающая вызовы остальных функций
def count_calls():
    global calls
    calls += 1

#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре
def string_info(string_param):
    count_calls()
    return tuple([len(string_param), string_param.upper(), string_param.lower()])

# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
def is_contains(string_param2, list_param):
    for i in range(0, len(list_param)):
        if string_param2.upper() == list_param[i].upper():
            return True
        elif i == len(list_param) - 1:
            return False


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
