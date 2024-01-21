'''
Хеширование цепочками

Хеширование цепочками — один из наиболее популярных методов реализации хеш-таблиц на практике. Ваша цель в данной задаче — реализовать такую схему, используя таблицу с m ячейками и полиномиальной хеш-функцией на строках

где S[i] — ASCII-код i-го символа строки S, p = 1 000 000 007 — простое число, x = 263. Ваша программа должна поддерживать следующие
типы запросов:
• add string: добавить строку string в таблицу. Если такая строка уже есть, проигнорировать запрос;
• del string: удалить строку string из таблицы. Если такой строки нет, проигнорировать запрос;
• find string: вывести «yes» или «no» в зависимости от того, есть в таблице строка string или нет;
• check i: вывести i-й список (используя пробел в качестве разделителя); если i-й список пуст, вывести пустую строку.
При добавлении строки в цепочку, строка должна добавляться в начало цепочки.

При добавлении строки в цепочку, строка должна добавляться в начало цепочки.

Формат входа.
Первая строка размер хеш-таблицы m. Следующая строка содержит количество запросов n. Каждая из последующих n строк содержит запрос одного из перечисленных выше четырёх типов.
Формат выхода.
Для каждого из запросов типа find и check выведите результат в отдельной строке.

Пример.
Вход:
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good

Выход:
HellO world
no
yes
HellO
GooD luck
ASCII коды букв w, o, r, l, d равны 119, 111, 114, 108, 100, соответственно.
Поэтому h(world) = (119 + 111 × 263 + 114 × 2632 + 108 × 2633 +100 × 2634 mod 1 000 000 007) mod 5 = 4.


Sample Input 2:
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test

Sample Output 2:
yes
no
no
yes
'''


import sys


class ChainHasher:
    m = 0
    p = 1000000007
    x = 263
    x_degrees = []
    chain = []

    def __init__(self, m):
        self.x_degrees = [ self.x**i for i in range(15) ]
        self.chain = [[] for i in range(m + 1)]
        self.m = m

    def hash(self, _string):
        sumOfChar = 0
        for i in range(len(_string)):
            sumOfChar += ((ord(_string[i]) * self.x_degrees[i]) % self.p)
        return (sumOfChar % self.p) % self.m

    def add(self, _string):
        idChain = self.hash(_string)
        id = self.find(_string, idChain)

        if id != -1:
            return

        self.chain[idChain] = [_string] + self.chain[idChain]

    def delete(self, _string):
        idChain = self.hash(_string)
        id = self.find(_string, idChain)

        if id == -1:
            return

        del self.chain[idChain][id]

    def find(self, _string, _id = None):
        idChain = self.hash(_string) if _id is None else _id
        try:
            idStr = self.chain[idChain].index(_string)
            return idStr
        except ValueError:
            return -1

    def check(self, id):
        return self.chain[id]


def main():
    chainHasher = None
    i = 0
    m = -1
    for line in sys.stdin:
        if i == 0:
            chainHasher = ChainHasher(int(line))
        elif i > 1:
            data = line.strip().split(' ')
            if data[0] == 'add':
                chainHasher.add(data[1])
            if data[0] == 'del':
                chainHasher.delete(data[1])
            if data[0] == 'find':
                id = chainHasher.find(data[1])
                print('no' if id == -1 else 'yes')
            if data[0] == 'check':
                _list = chainHasher.check(int(data[1]))
                print(' '.join(_list))

        i += 1


if __name__ == '__main__':
    main()