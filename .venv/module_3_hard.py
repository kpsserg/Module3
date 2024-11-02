def sum_of_str(str_param):
    global lst
    str_param = int(len((str_param)))
    lst.append(str_param)

def sum_of_int(int_param):
    global lst
    lst.append(int_param)

def sum_of_dict(dict_param):
    for key, value in dict_param.items():
        if isinstance(key, int):
            sum_of_int(key)
        elif isinstance(key, str):
            sum_of_str(key)
        if isinstance(value, int):
            sum_of_int(value)
        elif isinstance(value, str):
            sum_of_str(value)


def build_list(data_):
    #print('\nФ-я build_list получила следующие данные', data_)
    #global lst
    if isinstance(data_, int):
        len_data = 1
    else:
        len_data = int(len(data_))
    for i in range(0, len_data):
        #print('Iteration #',  [i],'have ', 'elements',data_[i])
        if isinstance(data_[i], str):
            #print('str', data_[i])
            sum_of_str(data_[i])
        elif isinstance(data_[i], int):
            sum_of_int(data_[i])
            #print('Integer ', data_[i])
        elif isinstance(data_[i], (list, tuple, set)):
            #print('Множество, кортеж или список',data_[i])
            build_list(data_[i])
        elif isinstance(data_[i], dict):
        #     pass
            #print('Dict', data_[i])
            sum_of_dict(data_[i])

lst = []
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), (2, 'Urban', ('Urban2', 35)))
]

build_list(data_structure)
print(sum(lst))

