'''
Дано неориентированное дерево, подвешенное за вершину 1. Для каждой вершины подсчитайте, сколько вершин содержится в поддереве, подвешенном за данную вершину.
Формат ввода
В первой строке вводится число V — количество вершин (3 ≤ V ≤ 100000)
В следующей строке записаны предки вершин с номерами от 2 до V. Число на i-ой позиции - предок вершины с номером i+1.
Формат вывода
Выведите V чисел — размеры поддеревьев для каждой из вершин

Sample Input:
3
1 2

Sample Output:
3 2 1



12
1 1 2 2 3 3 6 4 4 10 10

12 7 4 5 1 2 1 1 1 3 1 1
'''



import sys
sys.setrecursionlimit(150000)

def printAnswer(n, parents):
    tree = [[] for i in range(n)]
    childs = [0] * n

    for i in range(n - 1):
        parentId = parents[i]
        tree[parentId].append(i + 1)

    def dfs(idx):
        count = 1
        for i in tree[idx]:
            if childs[i] == 0:
                count += dfs(i)
            else:
                count += childs[i]
        childs[idx] = count
        return count

    for i in reversed(range(n)):
        dfs(i)

    print(' '.join([str(i) for i in childs]))

def main():
    n = -1
    data = []
    for line in sys.stdin:
        if n == -1:
            n = int(line)
        else:
            data = [int(i) - 1 for i in line.strip().split(' ')]

    printAnswer(n, data)


if __name__ == '__main__':
    main()

