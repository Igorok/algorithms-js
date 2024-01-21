'''
По заданной матрице смежности неориентированного графа найдите количество петель, которое он содержит.

Входные данные
На вход программы поступает число n (<= 100) - количество вершин графа, а затем n строк по n чисел, каждое из которых равно 0 или 1, - его матрица смежности.

Выходные данные
Одно число - количество петель в графе.

Sample Input:
5
1 1 1 1 0
1 0 1 1 1
1 1 0 1 1
1 1 1 1 1
0 1 1 1 0

Sample Output:
2
'''

import sys

def getLoopsNumber(n, matrix):
    loops = 0
    for i in range(0, n):
        if matrix[i][i] == 1:
            loops += 1

    return loops

def main():
    n = None
    matrix = []
    for line in sys.stdin:
        data = [int(i) for i in line.split(' ')]
        if n is None:
            n = data[0]
        else:
            matrix.append(data)
    print(getLoopsNumber(n, matrix))


if __name__ == '__main__':
    main()