def get_multiplied_digits(number):
    global c
    str_number = str(number)
    if len(str_number) == 1 and c and int(str_number[0]) == 0: #условие для последнего нуля, чтобы не обнулить результат
        return 1
    elif len(str_number) == 1:
        return int(str_number)
    c = True
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))


c = False
result = get_multiplied_digits(1012345)
print(result)