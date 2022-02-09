# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random

array = [random.randint(-100, 99) for _ in range(10)]
print(array)

def bubble_sorting(array):
    n=1
    while n<len(array):
        for i in range(len(array)-n):
            if array[i]>array[i+1]:
                array[i], array[i+1]=array[i+1], array[i]
        n+=1
    return array

bubble_sorting(array)
print(array)