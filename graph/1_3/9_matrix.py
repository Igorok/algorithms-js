'''
По заданной матрице смежности ориентированного графа найдите количество ребер в нем.

Входные данные
На вход программы поступает число n (<= 100) - количество вершин графа, а затем n строк по n чисел, каждое из которых равно 0 или 1, - его матрица смежности.

Выходные данные
Одно число - количество ребер в графе.

Sample Input:
5
0 0 0 0 0
0 0 0 0 1
1 1 0 0 0
0 0 0 0 0
0 0 0 0 0

Sample Output:
3
'''


import sys

def getEdgesNumber(n, matrix):
    edges = 0
    for i in range(n):
        edges += sum(matrix[i]) - matrix[i][i]

    return edges

def main():
    n = None
    matrix = []
    for line in sys.stdin:
        data = [int(i) for i in line.strip().split(' ')]
        if n is None:
            n = data[0]
        else:
            matrix.append(data)
    print(getEdgesNumber(n, matrix))


if __name__ == '__main__':
    main()