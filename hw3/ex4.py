# Определить, какое число в массиве встречается чаще всего.

import random
size=20
num_list=[random.randint(0,size//5) for i in range(size)]
frequency_list={}
num=0

for i in range(size-1):
    frequency_count = 0
    num=num_list[i+1]
    for i in num_list:
        if num==num_list[i]:
            frequency_count+=1
            frequency_list[num_list[i]]=frequency_count
num=0
for v in frequency_list.values():
    if num<v:
        num=v
for k, v in frequency_list.items():
    if num==v:
        print(f'чаще всего в массиве встречается число "{k}": {v} раз.')
print(num_list)
print(frequency_list)


