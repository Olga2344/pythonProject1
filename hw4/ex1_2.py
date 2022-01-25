
#4. Определить, какое число в массиве встречается чаще всего.

import random
# вариант 2

def task_2():
    my_dict = {}
    size = 2000
    my_list = [random.randint(0,size//5) for i in range(size)]
    # print(my_list)
    set_my_list = list(set(my_list))
    # print(set_my_list)
    for i in set_my_list:
        my_dict[i] = 0
    for i in my_list:
        my_dict[i] += 1
    max_el = set_my_list[0]
    max_ind = 0
    for i in my_dict.keys():
        if my_dict[i] > max_el:
            max_el = my_dict[i]
            max_ind = i
    # print(f'Элемент {max_ind} чаще всего повторяется. Он встречается {max_el} раз')