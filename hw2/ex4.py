# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

line_len=int(input('длинна ряда: '))
sum_elem=0
elem=1
for i in range(line_len):
    sum_elem+=elem
    elem/= -2
print(sum_elem)