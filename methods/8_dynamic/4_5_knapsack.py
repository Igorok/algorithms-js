'''
Задача на программирование: рюкзак

Первая строка входа содержит целые числа 1 <= W <= 10^4 и 1 <= n <= 300 — вместимость рюкзака и число золотых слитков.
Следующая строка содержит n целых чисел 0 <= w[i], ..., w[n] <= 10^5, задающих веса слитков. Найдите максимальный вес золота, который можно унести в рюкзаке.

Sample Input:
10 3
1 4 8

Sample Output:
9
'''



'''.git/

[
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5],
    [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9]
]

'''


import sys


def get_weight(W, n, items):
    d = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for j in range(1, W + 1):
            d[i][j] = d[i - 1][j]
            if item <= j:
                d[i][j] = max(
                    d[i - 1][j],
                    item + d[i - 1][max(j - item, 0)],
                )

    return d[n][W]


def main():
    data = []
    for line in sys.stdin:
        data.append([int(i) for i in line.split(' ')])

    weight = get_weight(data[0][0], data[0][1], data[1])
    print(weight)


def test():
    assert get_weight(10, 3, [1, 4, 8]) == 9
    assert get_weight(10, 0, []) == 0
    assert get_weight(0, 2, [1, 2]) == 0
    assert get_weight(16, 3, [10, 5, 1]) == 16


if __name__ == '__main__':
    main()
