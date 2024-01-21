'''
Неориентированный граф без петель и кратных рёбер задан матрицей смежности.
выведите его представление в виде списка ребер.
Входные данные
Входные данные включают число n (1 <= n <= 100 ) - количество вершин в графе, а затем n строк по n чисел, каждое из которых равно 0 или 1, - его матрицу смежности.
Выходные данные
Выведите список ребер заданного графа в отсортированном порядке. По одному ребру на каждой строке.

Sample Input:
5
0 0 1 0 0
0 0 1 0 1
1 1 0 0 0
0 0 0 0 0
0 1 0 0 0

Sample Output:
1 3
2 3
2 5
'''

import sys

def printAnswer(n, matrix):
    ribs = []
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and i < j:
                print('{} {} '.format(i+1, j+1))

def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[1:])


if __name__ == '__main__':
    main()