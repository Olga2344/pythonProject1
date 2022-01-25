#4. Определить, какое число в массиве встречается чаще всего.

import random
import cProfile
import timeit


#  вариант 1
def task_1():
    size = 2000
    num_list = [random.randint(0,size//5) for i in range(size)]
    frequency_list = {}

    for i in range(size - 1):
        frequency_count = 0
        num = num_list[i + 1]
        for i in num_list:
            if num == num_list[i]:
                frequency_count += 1
                frequency_list[num_list[i]] = frequency_count
    num = 0
    for v in frequency_list.values():
        if num < v:
            num = v
    for k, v in frequency_list.items():
        if num == v:
            num=v
            # print(f'чаще всего в массиве встречается число "{k}": {v} раз.')
    # print(num_list)
    # print(frequency_list)

#
# # вариант 2
# def task_2():
#     my_dict = {}
#     size = 2000
#     my_list = [random.randint(0,size//5) for i in range(size)]
#     # print(my_list)
#     set_my_list = list(set(my_list))
#     # print(set_my_list)
#     for i in set_my_list:
#         my_dict[i] = 0
#     for i in my_list:
#         my_dict[i] += 1
#     max_el = set_my_list[0]
#     max_ind = 0
#     for i in my_dict.keys():
#         if my_dict[i] > max_el:
#             max_el = my_dict[i]
#             max_ind = i
#     # print(f'Элемент {max_ind} чаще всего повторяется. Он встречается {max_el} раз')

# # вариант 3
# def task_3():
#     size = 2000
#     rand_mas = [random.randint(0,size//5) for i in range(size)]
#     b = 0
#     a = 0
#     for i in rand_mas:
#         if rand_mas.count(i) > b:
#             b = rand_mas.count(i)
#             a = i
#     # print(f'В массиве чаще всего встречается число {a}')

# def main():
#     a=task_1()
#     b=task_2()
#     c=task_3()

# cProfile.run('main()')


'''
cProfile
         33679 function calls in 1.278 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.278    1.278 <string>:1(<module>)
        1    0.001    0.001    0.013    0.013 ex1.py:31(task_2)
        1    0.002    0.002    0.012    0.012 ex1.py:34(<listcomp>)
        1    0.002    0.002    0.248    0.248 ex1.py:51(task_3)
        1    0.002    0.002    0.024    0.024 ex1.py:53(<listcomp>)
        1    0.998    0.998    1.017    1.017 ex1.py:6(task_1)
        1    0.000    0.000    1.278    1.278 ex1.py:62(main)
        1    0.002    0.002    0.019    0.019 ex1.py:8(<listcomp>)
     6000    0.020    0.000    0.024    0.000 random.py:237(_randbelow_with_getrandbits)
     6000    0.022    0.000    0.046    0.000 random.py:290(randrange)
     6000    0.005    0.000    0.051    0.000 random.py:334(randint)
        1    0.000    0.000    1.278    1.278 {built-in method builtins.exec}
     6000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
     2003    0.222    0.000    0.222    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     7663    0.003    0.000    0.003    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}



Process finished with exit code 0
'''

'''
timeit

(HW) MacBook-Olga:hw4 olga$ python -m timeit -s "import ex1"
10000000 loops, best of 5: 21.6 nsec per loop
(HW) MacBook-Olga:hw4 olga$ python -m timeit -n 10 -s "import ex1"
10 loops, best of 5: 41 nsec per loop
:0: UserWarning: The test results are likely unreliable. The worst time (171 nsec) was more than four times slower than the best time (41 nsec).
(HW) MacBook-Olga:hw4 olga$ python -m timeit -n 10 -s "import ex1"
10 loops, best of 5: 44.5 nsec per loop
:0: UserWarning: The test results are likely unreliable. The worst time (217 nsec) was more than four times slower than the best time (44.5 nsec).
(HW) MacBook-Olga:hw4 olga$ python -m timeit -n 100 -s "import ex1"
100 loops, best of 5: 23.1 nsec per loop
(HW) MacBook-Olga:hw4 olga$ python -m timeit -n 100 -s "import ex1_2"
100 loops, best of 5: 22.6 nsec per loop
(HW) MacBook-Olga:hw4 olga$ python -m timeit -n 100 -s "import ex1_3"
100 loops, best of 5: 23.5 nsec per loop


'''