my_int = 100
my_float = 5.5
my_str = "Я строка"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'Город': 'Ессентуки', 'Урок': 'Второй'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')