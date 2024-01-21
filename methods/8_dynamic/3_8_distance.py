'''
Задача на программирование: расстояние редактирования

Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2, содержащих строчные буквы латинского алфавита.

Sample Input 1:
ab
ab

Sample Output 1:
0

Sample Input 2:
short
ports

Sample Output 2:
3
'''

import sys


def get_distance(lines):
    s1, s2 = lines[0], lines[1]
    m, n = len(s1), len(s2)
    d = [ [0] * (n + 1) for _ in range(m + 1) ]

    for i in range(m + 1):
        d[i][0] = i

    for j in range(n + 1):
        d[0][j] =j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d[i][j] = min(
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + (s1[i - 1] != s2[j - 1])
            )

    return d[m][n]


def main():
    data = []
    for line in sys.stdin:
        data.append(line)

    distance = get_distance(data)
    print(distance)


def test():
    assert get_distance(['ab', 'ab']) == 0
    assert get_distance(['short', 'ports']) == 3
    assert get_distance(['', '12345']) == 5
    assert get_distance(['12345', '']) == 5


if __name__ == '__main__':
    main()
