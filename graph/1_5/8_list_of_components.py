'''
Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо вывести все компоненты связности.
Входные данные
Во входном файле записано два числа N и M (0 < N <= 100000, 0 <= M <= 100000). В следующих M строках записаны по два числа i и j (1 <= i, j <= N), которые означают, что вершины i и j соединены ребром.
Выходные данные
В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в отсортированном порядке. Компоненты связности должны быть отсортированы по возрастанию минимального номера вершины из этой компоненты.

Sample Input 1:
6 4
3 1
1 2
5 4
2 3

Sample Output 1:
3
3
1 2 3
2
4 5
1
6

Sample Input 2:
6 4
4 2
1 4
6 4
3 6

Sample Output 2:
2
5
1 2 3 4 6
1
5
'''


import sys

def findComponent(used, nodes, node):
    queue = [node]
    components = []
    while len(queue) > 0:
        value = queue.pop()
        if used[value] == 1:
            continue
        used[value] = 1
        components.append(value)
        for i in nodes[value]:
            if value == i:
                components.append(i)
            elif used[i] == 0:
                queue.append(i)

    return [
        used,
        nodes,
        sorted(components),
    ]


def findNotUsed(used, pastUsed):
    for i in range(pastUsed, len(used)):
        if used[i] == 0:
            return i
    return -1


def printAnswer(n, m, edges):
    used = [0]*n
    nodes = [[] for i in range(n)]

    for i, j in edges:
        nodes[i-1].append(j-1)
        nodes[j-1].append(i-1)

    allComponents = []
    notUsed = findNotUsed(used, 0)
    while notUsed != -1:
        used, nodes, components = findComponent(used, nodes, notUsed)
        allComponents.append(components)
        notUsed = findNotUsed(used, notUsed)

    print(len(allComponents))
    for components in allComponents:
        print(len(components))
        print(' '.join([str(i + 1) for i in components]) + ' ')


def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[0][1], data[1:])


if __name__ == '__main__':
    main()