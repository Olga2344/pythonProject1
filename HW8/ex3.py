import random


def get_graph(c):
    result = []
    all_nodes = {i for i in range(c)}
    for i in range(c):
        result.append(random.sample(list(all_nodes - {i}), random.randint(1, c - 1)))
    return result


def dfs(g, node, v=[]):
    v.append(node)
    for n in g[node]:
        if n not in v:
            dfs(g, n, v)
    return v


count = int(input('Число вершин: '))
start = int(input('Начальная вершина: '))
graph = get_graph(count)
print('Исходный граф: ', graph)
print('Обход графа: ', dfs(graph, start))