# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы,
# в другой — не больше медианы.
import random

m = 10
array = [random.randint(1, 50) for _ in range(2 * m + 1)]


def gnome_sort(data):
    i = 1
    size = len(data)
    while i < size:
        if data[i - 1] <= data[i]:
            i += 1
        else:
            data[i - 1], data[i] = data[i], data[i - 1]
            if i > 1:
                i -= 1
    return data

print(array)

array_sorted = (gnome_sort(array))
print(array_sorted)
print(f'\nМедиана: "index": {m}, "value": {array_sorted[m]}')