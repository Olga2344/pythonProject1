# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

hex_dict={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


hex_1=['A', '2']
hex_2=['C', '4', 'F']


def transfer_to_10(num):
    transfer_hex=0
    num.reverse()
    for i, k in enumerate(num):
        transfer_hex+=hex_dict.get(k)*16**(i)
    return transfer_hex

def get_key(val):
    for key, value in hex_dict.items():
         if val == value:
             return key


def transfer_to_16(num):
    transfer_hex=[]
    if num<16:
        transfer_hex.append(get_key(num))
    else:
        while num > 0:
            transfer_hex.append(get_key(num % 16))
            num = num // 16
    transfer_hex.reverse()
    return transfer_hex

n1=transfer_to_10(hex_1)
n2=transfer_to_10(hex_2)
print(n1)
print(n2)

hex_sum=n1+n2

print(transfer_to_16(hex_sum))



