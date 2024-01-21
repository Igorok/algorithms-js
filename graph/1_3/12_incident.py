'''
Неориентированный граф задаётся списком ребер. Необходимо посчитать количество рёбер, инцидентных данному. То есть имеющих с ним одну общую вершину.
Входные данные
Сначала вводятся числа n – количество вершин в графе и m – количество ребер. Затем следует m пар чисел – ребра графа.
Далее в отдельной строке вводится число k - номер ребра.
Выходные данные
Выведите одно число - количество ребер, инцидентных k-ому.

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

def getAnswer(data):
    n = data[0][0]
    m = data[0][1]

    edges = [0]*(n+1)
    for i in range(1, m + 1):
        first, second = data[i]
        edges[first] += 1
        edges[second] += 1

    first, second = data[data[-1][0]]

    return edges[first] + edges[second] - 2


def main():
    data = []
    for line in sys.stdin:
        numbers = [int(i) for i in line.strip().split(' ')]
        data.append(numbers)
    answer = getAnswer(data)
    print(answer)


if __name__ == '__main__':
    main()