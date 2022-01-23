# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random
size=20
num_list=[random.randint(-size,size) for i in range(size)]
num_min=num_list[0]
num_max=0
indx_min=0
indx_max =0
sum_num=0
for i,v in enumerate(num_list):
    if num_min>v:
        num_min=v
        indx_min=i
    if num_max < v:
        num_max = v
        indx_max=i
if indx_min<indx_max:
    for i in num_list[indx_min+1:indx_max]:
        sum_num+=i
else:
    for i in num_list[indx_max:indx_min+1]:
        sum_num+=i
# else:
#     print('между индексами нет чисел')
print(num_list[indx_min+1:indx_max])
print(num_list)
print(sum_num)