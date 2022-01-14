# 8. Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого).

num_1 = int(input('введите число '))
num_2 = int(input('введите число '))
num_3 = int(input('введите число '))

if num_1 > num_2 > num_3 or num_1 < num_2 < num_3:
        print(f'среднее число {num_2}')
elif num_2 > num_1 > num_3 or num_2 < num_1 < num_3:
        print(f'среднее число {num_1}')
else:
        print(f'среднее число {num_3}')



