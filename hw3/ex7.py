# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

import random
size=10
num_list=[random.randint(1,size) for i in range(size)]
num_min = num_list[0]
num_min1 = num_list[0]

print(num_list)
for v in num_list:
    if num_min > v:
        num_min = v

num_list.remove(num_min)

for i in num_list:
    if num_min1 > i:
        num_min1 = i

print(f'первое минимальное число {num_min}, второе минимальное число {num_min1}')
print(num_list)

