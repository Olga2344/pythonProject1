# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
size=20
num_list=[random.randint(-size,size) for i in range(size)]
negative_num_list=[]

for i in num_list:
    if i <0:
        negative_num_list.append(i)

num_max=negative_num_list[0]

for i in range(len(negative_num_list)):
    if num_max<negative_num_list[i]:
        num_max=negative_num_list[i]
print(num_max)
print(negative_num_list)
print(num_list)