# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.

import sys, cProfile


def prime(num):
    count = 1
    num_list = [2]
    test_num_list = []
    for i in range(3, sys.maxsize ** 10, 2):
        j = i * 2
        test_num_list.append(j + i)
        test_num_list.append(i ** 2)
        if i > 5 and i % 5 == 0:
            test_num_list.append(i)

        if i not in test_num_list:
            num_list.append(i)
            count += 1

        if count == num:
            return i

u_number=20
print(prime(u_number))
cProfile.run('prime(u_number)')

'''

100 loops, best of 5: 28.6 nsec per loop
1000 loops, best of 5: 21 nsec per loop

99 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 ex2.py:8(prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       95    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''