'''
Имеется неориентированный граф, состоящий из N вершин и M ребер. Необходимо проверить, является ли граф деревом. Напомним, что дерево — это связный граф, в котором нет циклов (следовательно, между любой парой вершин существует ровно один простой путь). Граф называется связным, если от одной вершины существует путь до любой другой.

Входные данные
Во входном файле в первой строке содержатся два целых числа N и M (1 ≤ N ≤ 100, 0 ≤ M ≤ 1000), записанные через пробел. Далее следуют M различных строк с описаниями ребер, каждая из которых содержит два натуральных числа Ai и Bi (1 ≤ Ai <Bi ≤ N), где Ai и Bi — номера вершин, соединенных i-м ребром.

Выходные данные
В выходной файл выведите слово YES, если граф является деревом или NO в противном случае.

Sample Input:
3 2
1 2
1 3

Sample Output:
YES
'''

import sys

def printAnswer(n, data):
    used = [-1] * n
    parents = [-1] * n

    stack = [[0, 0]]
    visited = 0
    while len(stack) > 0:
        value, parent = stack.pop()
        if parents[value] != -1:
            print('NO')
            return

        parents[value] = parent
        used[value] = 1
        visited += 1
        for i in data[value]:
            if used[i] == -1:
                stack.append([i, value])

    print('YES') if visited == n else print('NO')

def main():
    n = -1
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        if n == -1:
            n = numbers[0]
            data = [[] for _ in range(n)]
        else:
            first = numbers[0] - 1
            second = numbers[1] - 1
            data[first].append(second)
            data[second].append(first)

    printAnswer(n, data)


if __name__ == '__main__':
    main()
