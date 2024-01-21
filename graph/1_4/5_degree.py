'''
Неориентированный граф задаётся списком ребер. Необходимо посчитать количество различных степеней вершин данного графа.
Входные данные
Сначала вводятся числа n - количество вершин в графе и m - количество ребер. Затем следует m пар чисел - ребра графа.
Выходные данные
Выведите одно число - количество различных степеней вершин графа.

Sample Input:
5 4
1 3
1 2
2 3
2 5

Sample Output:
4

'''

import sys

def printAnswer(n, m, ribs):
    degrees = [0]*n

    for rib in ribs:
        i, j = rib
        i -= 1
        j -= 1
        degrees[i] += 1
        degrees[j] += 1

    print(len(set(degrees)))


def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[0][1], data[1:])


if __name__ == '__main__':
    main()