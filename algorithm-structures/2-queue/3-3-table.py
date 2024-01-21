'''
Системы непересекающихся множеств

Объединение таблиц

Ваша цель в данной задаче — реализовать симуляцию объединения таблиц в базе данных.
В базе данных есть n таблиц, пронумерованных от 1 до n, над одним и тем же множеством столбцов (атрибутов). Каждая таблица содержит либо реальные записи в таблице, либо символьную ссылку на другую таблицу. Изначально все таблицы содержат реальные записи, и i-я таблица содержит r[i] записей. Ваша цель — обработать m запросов типа (destination[i] , source[i]):

1. Рассмотрим таблицу с номером destination[i] . Пройдясь по цепочке символьных ссылок, найдём номер реальной таблицы, на которую ссылается эта таблица:
пока таблица destination[i] содержит символическую ссылку:
destination[i] - symlink(destination[i])

2. Сделаем то же самое с таблицей source[i].

3. Теперь таблицы destination[i] и source[i] содержат реальные записи. Если destination[i] != source[i] , скопируем все записи из таблицы source[i] в таблицу destination[i] , очистим таблицу source[i] и пропишем в неё символическую ссылку на таблицу destination[i].

4. Выведем максимальный размер среди всех n таблиц. Размером таблицы называется число строк в ней. Если таблица содержит символическую ссылку, считаем её размер равным нулю.

Формат входа.
Первая строка содержит числа n и m — число таблиц и число запросов, соответственно. Вторая строка содержит n целых чисел r[1], . . . , r[n] — размеры таблиц. Каждая из последующих m строк содержит два номера таблиц destination[i] и source[i] , которые необходимо объединить.

Формат выхода.
Для каждого из m запросов выведите максимальный размер таблицы после соответствующего объединения.

Ограничения.
1 <= n, m <= 100 000; 0 <= r[i] <= 10 000; 1 <= destination[i] , source[i] <= n.

Sample Input:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3

Sample Output:
2
2
3
5
5

Изначально каждая таблица содержит ровно одну строку.
1. После первой операции объединения все записи из таблицы 5 копируются в таблицу 3. Теперь таблица 5 является ссылкой на таблицу 3, а таблица 3 содержит две записи.
2. Вторая операция аналогичным образом переносит все записи из таблицы 2 в таблицу 4.
3. Третья операция пытается объединить таблицы 1 и 4, но таблица 4 ссылается на таблицу 2, поэтому все записи из таблицы 2 копируются в таблицу 1. Таблица 1 теперь содержит три строки.
4. Чтобы произвести четвёртую операцию, проследим пути из ссылок: 4 → 2 → 1 и 5 → 3. Скопируем все записи из таблицы 1 в таблицу 3, после чего в таблице 3 будет пять записей.
5. После этого все таблицы ссылаются на таблицу 3, поэтому все оставшиеся запросы объединения ничего не меняют.

Вход:
6 4
10 0 5 0 3 3
6 6
6 5
5 4
4 3

Выход:
10
10
10
11

1. Запрос объединения таблицы 6 с собой ничего не меняет, максимальным размером по-прежнему остаётся 10 (таблица 1).
2. Записи из таблицы 5 копируются в таблицу 6, размер таблицы 6 становится равным 6.
3. Записи из таблицы 4 копируются в таблицу 6, размер таблицы 6 становится равным 10.
4. Записи из таблицы 3 копируются в таблицу 6, размер таблицы 6 становится равным 11.
'''


import sys


class DisJoinSetManager:
    parents = []
    rank = []
    maxSize = 0

    def __init__(self, n, sizes):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
        self.sizes = sizes
        self.maxSize = max(self.sizes)

    def find(self, i):
        while self.parents[i] != i:
            i = self.parents[i]
        return i

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return self.maxSize

        if self.rank[parentX] > self.rank[parentY]:
            self.parents[parentY] = parentX
            self.sizes[parentX] += self.sizes[parentY]
            self.sizes[parentY] = 0
            if self.sizes[parentX] > self.maxSize:
                self.maxSize = self.sizes[parentX]
            return self.maxSize

        if self.rank[parentY] > self.rank[parentX]:
            self.parents[parentX] = parentY
            self.sizes[parentY] += self.sizes[parentX]
            self.sizes[parentX] = 0
            if self.sizes[parentY] > self.maxSize:
                self.maxSize = self.sizes[parentY]
            return self.maxSize

        if self.rank[parentX] == self.rank[parentY]:
            self.parents[parentY] = parentX
            self.rank[parentX] += 1
            self.sizes[parentX] += self.sizes[parentY]
            self.sizes[parentY] = 0
            if self.sizes[parentX] > self.maxSize:
                self.maxSize = self.sizes[parentX]
            return self.maxSize

def getUnionResult(n, m, sizes, unions):
    joinManger = DisJoinSetManager(n, sizes)
    for union in unions:
        r = joinManger.union(union[0] - 1, union[1] - 1)
        print(r)


def main():
    unions = []
    sizes = []
    n = 0
    m = 0
    i = 0
    for line in sys.stdin:
        data = [int(i) for i in line.split(' ')]
        if i == 0:
            n, m = data[0], data[1]
        elif i == 1:
            sizes = data
        else:
            unions.append(data)
        i += 1

    getUnionResult(n, m, sizes, unions)


if __name__ == '__main__':
    main()
