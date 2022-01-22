# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. Программа должна вычислять
# сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести
# полученную матрицу.


size=2
num_array=[]

for i in range(size):
    row=[]
    sum_line=0
    print(f'строка № {i+1}')
    for j in range(size):
        n=int(input('введите '))
        row.append(n)
        sum_line+=n
        if j==size-1:
            row.append(sum_line)
    num_array.append(row)

for i in range(len(num_array)):
    print(num_array[i])
