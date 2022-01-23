# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому
# из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

num_list=[i for i in range(2,100)]
short_list=[i for i in range(2,10)]
a=[0]*8

for i in short_list:
    for j in num_list:
        if j%i==0:
            a[i-2]+=1

for i in range(len(short_list)):
    print(f'{short_list[i]} - {a[i]},', end=' ')
