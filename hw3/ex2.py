# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
import random

num_list=[random.randint(0,100) for i in range(10)]
index_list=[]

for i, item in enumerate(num_list):
    if item%2==0:
        index_list.append(i)
print(num_list)
print(index_list)