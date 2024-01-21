'''
Дан ориентированный граф. Требуется определить, есть ли в нем цикл.

Входные данные
В первой строке вводится число вершин N <= 50. Далее в N строках следуют по N чисел, каждое из которых - 0 или 1. j-ое число в i-ой строке равно 1 тогда и только тогда, когда существует ребро, идущее из i-ой вершины в j-ую. Гарантируется, что на диагонали матрицы будут стоять нули.

Выходные данные
Выведите 0, если в заданном графе цикла нет, и 1, если он есть.

Sample Input:
3
0 1 0
0 0 1
0 0 0

Sample Output:
0
'''


import sys

def findNotUsed(used, start):
    for i in range(start, len(used)):
        if used[i] == -1:
            return i
    return -1


def printAnswer(n, data):
    used = [-1] * n
    start = 0
    stack = [start]
    while start != -1:
        track = [-1] * n
        while len(stack) > 0:
            value = stack.pop()
            used[value] = 1
            track[value] = 1
            for i in data[value]:
                if used[i] == -1:
                    stack.append(i)
                elif track[i] != -1:
                    print(1)
                    return
        start = findNotUsed(used, start)
        stack.append(start)

    print(0)


def main():
    i = -1
    n = -1
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        if i == -1:
            n = numbers[0]
            data = [[] for _ in range(n)]
        else:
            for j in range(n):
                if numbers[j] == 1:
                    data[i].append(j)
        i += 1
    printAnswer(n, data)


if __name__ == '__main__':
    main()


