'''
Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности, содержащую первую вершину.
Входные данные
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.
Выходные данные
В первой строке выведите число K - количество вершин в искомой компоненте.
В следующей строке через пробел выведите отсортированные по возрастанию номера вершин, которые принадлежат той же компоненте связности, что и первая вершина (включая первую вершину).
'''


import sys

def printAnswer(n, m, edges):
    used = [False]*n
    nodes = [[] for i in range(n)]

    for i, j in edges:
        nodes[i-1].append(j-1)
        nodes[j-1].append(i-1)

    queue = [0]
    answer = []
    while len(queue) > 0:
        value = queue.pop()
        if used[value]:
            continue
        used[value] = True
        answer.append(value)
        for i in nodes[value]:
            if value == i:
                answer.append(i)
            elif not used[i]:
                queue.append(i)
    print(len(answer))
    print(' '.join([str(i+1) for i in sorted(answer)]))

def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[0][1], data[1:])


if __name__ == '__main__':
    main()

