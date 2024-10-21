def single_root_words(a, *args):
    same_words = []
    print(f'{args}')
    for second_param_value in args:
        if a.upper() in second_param_value.upper() or second_param_value.upper() in a.upper():
            same_words.append(second_param_value)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

