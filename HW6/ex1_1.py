# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
import sys

Dict_company = namedtuple('company', ['name', 'quart_1', 'quart_2', 'quart_3', 'quart_4', 'total'])
comp_1 = Dict_company('sunrise', 123, 1231, -123, 124, 0)
comp_2 = Dict_company('eclipse', 1223, 1231, -123, 124, 0)
comp_3 = Dict_company('sunset', 153, 1241, -123, 124, 0)
comp_4 = Dict_company('midday', 125, 1931, 123, 124, 0)

comp_list = [comp_1, comp_2, comp_3, comp_4]
profit = []
less_average_list = []
more_average_list = []
average_2=0


def count(Dict_company):
    total_count = Dict_company.quart_1+Dict_company.quart_2+Dict_company.quart_3+Dict_company.quart_4
    return Dict_company._replace(total=total_count)

for i, n in enumerate(comp_list):
    comp_list[i]=count(n)

for i in comp_list:
    average_2+=i.total

average_2=average_2/len(comp_list)

for i, n in enumerate(comp_list):
    if average_2>=n.total:
        less_average_list.append(n.name)
    else:
        more_average_list.append(n.name)

print(f'наименования предприятий, чья прибыль выше среднего: {", ".join(more_average_list)} ')
print(f'наименования предприятий, чья прибыль ниже среднего: {", ".join(less_average_list)}')

sum_size =0
for e in [more_average_list, less_average_list, comp_list,average_2, Dict_company, comp_1, comp_2, comp_3, comp_4]:
    sum_size+=sys.getsizeof(e)
    print(f'  размер {sys.getsizeof(e)}')
print(sum_size)

'''
  размер 88
  размер 88
  размер 88
  размер 24
  размер 896
  размер 88
  размер 88
  размер 88
  размер 88
1536
'''