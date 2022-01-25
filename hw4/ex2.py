# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.

import sys

n=20
count=1
num_list = [2]
test_num_list=[]
for i in range(3, sys.maxsize**10, 2):
    j = i * 2
    test_num_list.append(j + i)
    test_num_list.append(i**2)
    if i>5 and i%5==0:
        test_num_list.append(i)

    if i not in test_num_list:
        num_list.append(i)
        count+=1

    if count == n:
        print(i)
        break


print(num_list)
print(test_num_list)

