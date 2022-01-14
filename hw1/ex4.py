# 4. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

alphabet='abcdefghijklmnopqrstuvwxyz'
letter_1= input('введите букву латинского алфавита: ')
letter_2= input('введите букву латинского алфавита: ')
num_letter_2 = alphabet.index(letter_2) + 1
num_letter_1 = alphabet.index(letter_1) + 1

dif_letters= num_letter_1 - num_letter_2

print(f'первая буква {letter_1} нахожится на позиции {num_letter_1}, '
      f'вторая буква {letter_2} на поизции {num_letter_2}, '
      f'между ними {dif_letters} букв')