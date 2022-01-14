# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

number_year = int(input(f'введите год '))

if number_year % 4 == 0 or number_year % 100 ==0:
    if number_year % 400 ==0 :
        print(f'{number_year} год = високосный век')
    else:
        print(f'{number_year} год високосный')
else:
    print(f'{number_year} год не високосный')