'''
Степенью вершины называется количество ребер, таких что данная вершина является одним из концов.

Задача
Неориентированный граф задан матрицей смежности. Необходимо посчитать количество вершин с нечетными и четными степенями.

Входные данные
На вход программы поступает число n (<= 100) - количество вершин графа, а затем n строк по n чисел, каждое из которых равно 0 или 1, - его матрица смежности.

Выходные данные
В одной строке выведите 2 числа: количество вершин с четной степенью и количество вершин с нечетной степенью.

Примечание
Обратите внимание, что петля увеличивает степень вершины на две единицы.

Sample Input:
5
1 1 1 1 0
1 0 1 1 1
1 1 0 1 1
1 1 1 1 1
0 1 1 1 0

Sample Output:
3 2
'''


import sys

def getDegreesNumber(n, matrix):
    degrees = [ (sum(matrix[i]) + matrix[i][i]) for i in range(n)]

    d1 = 0
    d2 = 0
    for i in degrees:
        if i != 0:
            if i % 2 == 0:
                d2 += 1
            else:
                d1 += 1

    return [d2, d1]

def main():
    n = None
    matrix = []
    for line in sys.stdin:
        data = [int(i) for i in line.strip().split(' ')]
        if n is None:
            n = data[0]
        else:
            matrix.append(data)
    degrees = getDegreesNumber(n, matrix)
    print(' '.join([str(i) for i in degrees]))


if __name__ == '__main__':
    main()