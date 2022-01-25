import cProfile


def eratosfen(number):
    array = [0, 0]
    n = 2

    while len(set(array)) < number + 1:
        array.append(n)
        i = 2
        while i < len(array):
            if array[i] != 0:
                j = i + i
                while j < len(array):
                    array[j] = 0
                    j = j + i
            i += 1
        n += 1
    array = list(set(array))
    array.remove(0)
    array.sort()
    return array[-1]


cProfile.run('eratosfen(20)')

'''
1000 loops, best of 5: 21 nsec per loop


6549 function calls in 0.008 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.008    0.008 <string>:1(<module>)
        1    0.007    0.007    0.008    0.008 ex2_1.py:4(eratosfen)
        1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
     6473    0.001    0.000    0.001    0.000 {built-in method builtins.len}
       70    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
'''