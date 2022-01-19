# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за
# 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randint

random_nam = randint(0, 100)
count_round = 0

while True:
    input_num = int(input(f'число от 0 до 100, у вас есть {10 - count_round} попыток: '))
    if random_nam == input_num:
        print('win!')
        break
    elif random_nam < input_num:
        print('загаданное число меньше')
        count_round += 1
    else:
        print('загаданное число больше')
        count_round += 1
    if count_round == 10:
        print(f'количеество попыток закончилось. загаданное число было = {random_nam}')
        break
