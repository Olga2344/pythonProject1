# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено
# число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number= int(input('введите число: '))
count_even=0
count_odd=0
while number>0:
    num_1= number%10
    if num_1%2 == 0:
        count_even+=1
    else:
        count_odd+=1
    print(num_1)
    number=number//10
print(f'количество четных чисел {count_even} и нечетных {count_odd}')

