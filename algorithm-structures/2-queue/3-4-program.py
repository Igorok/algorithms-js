'''
Автоматический анализ программ

При автоматическом анализе программ возникает такая задача.

Система равенств и неравенств
Проверить, можно ли присвоить переменным целые значения, чтобы выполнить заданные равенства вида x[i] = x[j] и неравенства вида x[p] != x[q].
Вход.
Число переменных n, а также список равенств вида x[i] = x[j] и неравенства вида x[p] != x[q].
Выход.
Проверить, выполнима ли данная система.

Формат входа.
Первая строка содержит числа n, e, d. Каждая из следующих e строк содержит два числа i и j и задаёт равенство x[i] = x[j]. Каждая из следующих d строк содержит два числа i и j и задаёт неравенство x[i] != x[j]. Переменные индексируются с 1: x[1], ..., x[n].

Формат выхода.
Выведите 1, если переменным x[1], ..., x[n] можно присвоить целые значения, чтобы все равенства и неравенства выполнились. В противном случае выведите 0.
Ограничения. 1 <= n <= 10^5 ; 0 <= e, d; e + d <= 2 * 10^5 ; 1 <= i, j <= n.

Пример.
Вход:
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4
Выход:
1

Пример.
Вход:
6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5
Выход:
0
'''


'''

1. n - массив с индексами 1-4
2. e - дальше будет массив числел, идет по нему столько ко то раз и пихаем в одно множество
3. d - после первого прохода идем вот столько то раз и проверяем что не принадлежит первому множеству
'''

import sys


class DisJoinSetManager:
    parents = []
    rank = []

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return

        if self.rank[parentX] > self.rank[parentY]:
            self.parents[parentY] = parentX
            return

        if self.rank[parentY] > self.rank[parentX]:
            self.parents[parentX] = parentY
            return

        if self.rank[parentX] == self.rank[parentY]:
            self.parents[parentY] = parentX
            self.rank[parentX] += 1
            return

def checkConditions(n, e, d, conditions):
    setManager = DisJoinSetManager(n)
    if e != 0:
        for i in range(e):
            setManager.union(
                conditions[i][0] - 1,
                conditions[i][1] - 1,
            )

    if d != 0:
        for i in range(e, e + d):
            parentX = setManager.find(conditions[i][0] - 1)
            parentY = setManager.find(conditions[i][1] - 1)
            if (parentX == parentY):
                print(0)
                return

    print(1)


def main():
    n = 0
    e = 0
    d = 0
    conditions = []

    i = 0
    for line in sys.stdin:
        data = [int(i) for i in line.split(' ')]
        if i == 0:
            n, e, d = data[0], data[1], data[2]
        else:
            conditions.append(data)
        i += 1

    checkConditions(n, e, d, conditions)


if __name__ == '__main__':
    main()