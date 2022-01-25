#4. Определить, какое число в массиве встречается чаще всего.
import random
# вариант 3
def task_3():
    size = 2000
    rand_mas = [random.randint(0,size//5) for i in range(size)]
    b = 0
    a = 0
    for i in rand_mas:
        if rand_mas.count(i) > b:
            b = rand_mas.count(i)
            a = i
    # print(f'В массиве чаще всего встречается число {a}')