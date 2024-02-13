'''
Дано дерево, подвешенное за вершину 1. Необходимо вывести все его листья в порядке возрастания.

Входные данные
В первой строке следует целое число n(2n100000) — количество соцветий.
Во второй строке следует последовательность целых чисел p2 p3 pn, состоящая из n−1  числа, где pi равно номеру предка вершины с номером i.

Выходные данные
Выведите номера вершин - листьев, в порядке возрастания

Sample Input:
3
1 2

Sample Output:
3
'''



'''.git/
3
1 2

v - 1 2 3
p - 1 2

i - 0 1 2
n - 1 2 3
p - ? 1 2


0 1 2 3
1 2


1 2 3
1 2
2 3


3
1 2

1 2 3



2 3 - index
1 2 - parent
1 2 3


'''

import sys


def printAnswer(n, parents):
    tree = [[] for i in range(n + 1)]
    for i in range(n - 1):
        tree[parents[i]].append(i + 2)

    leasts = []
    for i in range(1, n + 1):
        nodes = tree[i]
        if not nodes:
            leasts.append(str(i))

    print(' '.join(leasts))




def main():
    n = -1
    data = []
    for line in sys.stdin:
        if n == -1:
            n = int(line)
        else:
            data = [int(i) for i in line.strip().split(' ')]

    printAnswer(n, data)


if __name__ == '__main__':
    main()


