def get_multiplied_digits(number):
    first = 1
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))
        return first
    elif int(str_number[0]) > 0:    #последний символ больше 0
        first *= int(str_number[0])
        return first
    else:
        return first


result = get_multiplied_digits(120120)

print(result)
