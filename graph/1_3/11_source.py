'''
Ориентированный граф задан матрицей смежности. Посчитайте количество истоков и стоков.
Истоком называется вершина, в которую не входит ни одно ребро.
Стоком называется вершина, из которой не исходит ни одного ребра.
Входные данные
На вход программы поступает число n (<= 100) - количество вершин графа, а затем n строк по n чисел, каждое из которых равно 0 или 1, - его матрица смежности.
Выходные данные
В одной строке выведите 2 числа: количество истоков и стоков.

Sample Input:
5
0 0 0 0 0
0 0 0 0 1
1 1 0 0 0
0 0 0 0 0
0 0 0 0 0

Sample Output:
2 3
'''

'''
<- vertical
1 - 1 (3)
2 - 1 (3)
3 - 0
4 - 0
5 - 1 (2)
Not receive - 3,4

-> horizont
1 - 0
2 - 1 (5)
3 - 2 (1,2)
4 - 0
5 - 0
Not move 1,4,5
'''

import sys

def getSourceDrain(n, matrix):
    source = 0
    drain = 0

    for i in range(n):
        s = sum(matrix[j][i] for j in range(n))
        if s == 0:
            source += 1
        d = sum(matrix[i][j] for j in range(n))
        if d == 0:
            drain += 1

    return [source, drain]

def main():
    n = None
    matrix = []
    for line in sys.stdin:
        data = [int(i) for i in line.strip().split(' ')]
        if n is None:
            n = data[0]
        else:
            matrix.append(data)
    degrees = getSourceDrain(n, matrix)
    print(' '.join([str(i) for i in degrees]))


if __name__ == '__main__':
    main()