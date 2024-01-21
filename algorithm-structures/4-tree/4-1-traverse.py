'''
Обход двоичного дерева
Построить in-order, pre-order и post-order обходы данного двоичного дерева.
Вход. Двоичное дерево.
Выход. Все его вершины в трёх разных порядках: in-order, pre-order и post-order.

In-order обход соответствует следующей рекурсивной процедуре, получающей на вход корень v текущего поддерева: произвести рекурсивный вызов для v.left, напечатать v.key, произвести рекурсивный вызов для v.right.
Pre-order обход: напечатать v.key, произвести рекурсивный вызов для v.left, произвести рекурсивный вызов для v.right.
Post-order: произвести рекурсивный вызов для v.left, произвести рекурсивный вызов для v.right, напечатать v.key.

Формат входа.
Первая строка содержит число вершин n. Вершины дерева пронумерованы числами от 0 до n-1. Вершина 0 является корнем. Каждая из следующих n строк содержит информацию о вершинах 0, 1, ..., n - 1: i-я строка задаёт числа key[i], left[i] и right[i], где key[i] — ключ вершины i, left[i] — индекс левого сына вершины i, а right[i] — индекс правого сына вершины i. Если у вершины i нет одного или обоих сыновей, соответствующее значение
равно -1.
Формат выхода.
Три строки: in-order, pre-order и post-order обходы.
Ограничения. 1 <= n <= 10^5 ; 0 <= key[i] <= 10^9 ; -1 <= left[i] , right[i] <= n - 1.
Гарантируется, что вход задаёт корректное двоичное дерево: в частности, если left[i] != -1 и right[i] != -1, то left[i] != right[i] ; никакая вершина не является сыном двух вершин; каждая вершина является потомком корня.

Вход:
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1
Выход:
1 2 3 4 5
4 2 1 3 5
1 3 2 5 4


Sample Input:
10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1

Sample Output:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
'''

import sys

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, data):
        self.tree = data
        self.inOrderResult = []
        self.preOrderResult = []
        self.postOrderResult = []

    def inOrder(self, node = None):
        if node is None:
            node = self.tree[0]

        key, left, right = node
        if left != -1:
            self.inOrder(self.tree[left])

        self.inOrderResult.append(key)

        if right != -1:
            self.inOrder(self.tree[right])

    def preOrder(self, node = None):
        if node is None:
            node = self.tree[0]

        key, left, right = node
        self.preOrderResult.append(key)

        if left != -1:
            self.preOrder(self.tree[left])
        if right != -1:
            self.preOrder(self.tree[right])

    def postOrder(self, node = None):
        if node is None:
            node = self.tree[0]

        key, left, right = node
        if left != -1:
            self.postOrder(self.tree[left])
        if right != -1:
            self.postOrder(self.tree[right])
        self.postOrderResult.append(key)


def main():
    data = []
    i = 0
    for line in sys.stdin:
        if i != 0:
            data.append([int(i) for i in line.split(' ')])
        i += 1
    bTree = BinaryTree(data)
    bTree.inOrder()
    bTree.preOrder()
    bTree.postOrder()
    print(' '.join([str(i) for i in bTree.inOrderResult]))
    print(' '.join([str(i) for i in bTree.preOrderResult]))
    print(' '.join([str(i) for i in bTree.postOrderResult]))


if __name__ == '__main__':
    main()