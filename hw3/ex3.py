# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
num_list=[random.randint(0,100) for i in range(10)]
num_min=num_list[0]
num_max=0
for i in range(len(num_list)):
    if num_min>num_list[i]:
        num_min=num_list[i]
    if num_max < num_list[i]:
        num_max = num_list[i]
print(num_list)
print(num_min)
print(num_max)