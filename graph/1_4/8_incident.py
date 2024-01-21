'''
Неориентированный граф задаётся списком ребер. Необходимо посчитать количество ребер, инцидентных данной вершине. То есть таких ребер, что заданная вершина является одним из концов.
Входные данные
Сначала вводятся числа n - количество вершин в графе и m - количество ребер. Затем следует m пар чисел - ребра графа.
В отдельной строке вводится число k - номер вершины.
Выходные данные
Выведите одно число - количество ребер, инцидентных вершине номер k.

Sample Input:
5 4
1 3
1 2
2 3
2 5
2

Sample Output:
3
'''

import sys

def printAnswer(n, m, k, ribs):
    edges = [0]*n
    for i, j in ribs:
        if i == k:
            edges[i - 1] += 1
        if j == k:
            edges[j - 1] += 1
    return print(sum(edges))

def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[0][1], data[-1][0], data[1:-1])

if __name__ == '__main__':
    main()
