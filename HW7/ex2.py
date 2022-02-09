# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

array = [random.randint(0, 49) for _ in range(10)]
print(array)

def merge_sorting(array):
    if len(array) == 1 or len(array) == 0:
        return array
    left_array = merge_sorting(array[ :len(array) // 2])
    right_array = merge_sorting(array[len(array) // 2: ])
    n = m = k = 0
    copy_array = [0] * (len(left_array) + len(right_array))
    while n < len(left_array) and m < len(right_array):
        if left_array[n] <= right_array[m]:
            copy_array[k] = left_array[n]
            n += 1
        else:
            copy_array[k] = right_array[m]
            m += 1
        k += 1
    while n < len(left_array):
        copy_array[k] = left_array[n]
        n += 1
        k += 1
    while m < len(right_array):
        copy_array[k] = right_array[m]
        m += 1
        k += 1
    for i in range(len(array)):
        array[i] = copy_array[i]
    return array

merge_sorting(array)
print(array)