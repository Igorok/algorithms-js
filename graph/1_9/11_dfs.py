'''
Дан граф. Обойдите его при помощи алгоритма с лекции и выведите вершины в прямом порядке - раньше выводится номер той вершины, в которую раньше вошли.

Входные данные
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.

Выходные данные
Выведите вершины графа в нужно порядке.

Sample Input:
6 5
4 3
3 2
4 1
1 5
5 2

Sample Output:
1 5 2 3 4
'''

import sys


def printAnswer(n, m, tree):
    used = [-1] * n

    stack = [0]
    answer = []
    while stack:
        idx = stack.pop()
        if used[idx] == -1:
            answer.append(str(idx + 1))
        used[idx] = 1
        for i in tree[idx]:
            if used[i] == -1:
                stack.append(i)

    print(' '.join(answer))


def main():
    n = -1
    m = -1
    tree = []
    for line in sys.stdin:
        arr = [int(i) for i in line.strip().split(' ')]
        if n == -1:
            n = arr[0]
            m = arr[1]
            tree = [[] for i in range(n)]
        else:
            i = arr[0] - 1
            j = arr[1] - 1
            tree[i].append(j)
            tree[j].append(i)


    printAnswer(n, m, tree)



if __name__ == '__main__':
    main()