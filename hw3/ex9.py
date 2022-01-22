# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

size = 6

num_array = [[random.randint(-size*2, size*2) for i in range(size)] for j in range(size)]

min_list = []
num_max =0
for i in num_array:
    num_min = i[0]
    for j in i:
        if j < num_min:
            num_min = j
    min_list.append(num_min)

num_max = min_list[0]

for i in min_list:
    if num_max < i:
        num_max = i

print('матрица')
# for i in range(len(num_array)):
#     print(num_array[i])

for row in num_array:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()
print('список минимальных чисел')
print(min_list)
print('максимальное из миимальных чисел')
print(num_max)
