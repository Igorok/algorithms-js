'''
Ориентированный граф задаётся списком ребер. Проверьте, что между любыми двумя различными вершинами существует ровно одно ребро.
Входные данные
Сначала вводятся числа n - количество вершин в графе и m - количество ребер. Затем следует m пар чисел - ребра графа.
Выходные данные
Выведите YES, если условие выполняется, и NO в противном случае.

Sample Input:
5 10
1 2
1 3
1 5
2 3
2 5
4 1
4 2
4 3
4 5
5 3

Sample Output:
YES

'''


import sys

def printAnswer(n, m, ribs):
    degrees = [0]*n
    for i, j in ribs:
        degrees[i - 1] += 1
        degrees[j - 1] += 1

    print('YES' if len(set(degrees)) == 1 else 'NO')

def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    printAnswer(data[0][0], data[0][1], data[1:])

if __name__ == '__main__':
    main()
