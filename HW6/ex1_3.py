'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за четыре квартала для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import defaultdict, namedtuple
import sys

company = defaultdict(dict)
all_profit = 0
higher = {}
middle = {}
below = {}

n = 4

for i in range(n):
    print(f'Введите данные предприятия № {i + 1}')
    name = input(f'Введите наименование предприятия: ')
    profit = sum(float(input(f'Введите прибыль предприятия за {i}-й квартал: ')) for i in range(1, 5))
    all_profit += profit
    company.update({name: round((profit), 2)})

average_profit = all_profit / n
print(f'Средняя прибыль за год для всех предприятий: {average_profit:.2f}')

for i in company:
    if company.get(i) < average_profit:
        below.update({i: company.get(i)})
    elif company.get(i) > average_profit:
        higher.update({i: company.get(i)})
    else:
        middle.update({i: company.get(i)})

print(f'Прибыль ниже среднего у предприятий: {below}')
print(f'Прибыль выше среднего у предприятий: {higher}')
# print(f'Прибыль равна средней у предприятий: {middle}')
sum_size =0
for e in [higher, below, middle, company, average_profit, n, i]:
    sum_size+=sys.getsizeof(e)
    print(f'  размер {sys.getsizeof(e)}')
print(sum_size)

'''
PyCharm 2021.2.4 (Community Edition)
Build #PC-212.5712.39, built on December 21, 2021
x86_64

macOS 10.11.6
Memory: 1024M
Cores: 2



  размер 64
  размер 64
  размер 232
  размер 240
  размер 24
  размер 28
652
'''