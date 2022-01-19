# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
count=0
number= input('введите число: ')
len_number=len(number)
reverse_number=''
# while len_number != 0:
#     reverse_number=reverse_number +number[len_number-1]
#     len_number-=1
for i in range(len_number):
    reverse_number = reverse_number + number[len_number-1]
    len_number-=1
print(f'число обратное по порядку входящих в него цифр {reverse_number}')
