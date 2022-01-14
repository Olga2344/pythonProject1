# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

alphabet='abcdefghijklmnopqrstuvwxyz'
num_letter= int(input('введите номе буквы латинского алфавита: '))

print(f'введный номер буквы {num_letter} это {alphabet[num_letter - 1]}')
