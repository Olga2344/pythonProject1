# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.
from functools import reduce
friends_amount=6
graph_hand=[[1 if j>i else 0 for i in range(friends_amount)] for j in range(friends_amount)]
# сам себе не пожимает, учитывем, что жмем руки один раз 1->2, а 2->1 уже нет
# sum_graph=sum([sum(graph_hand[i]) for i in range(friends_amount)])
sum_graph=reduce(lambda x,y: x+sum(y), graph_hand,0)
print(f'всего рукопожатий: {sum_graph}')
print(*graph_hand, sep='\n')

