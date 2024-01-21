'''
Greedy algorithms

1. Looking for main feature - right end for an interval or price for a kilo for a backpack.
2. Sorting of items by main feature.
3. Selection of solutions
'''

'''
Задача на программирование: покрыть отрезки точками
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков содержит хотя бы одну из точек. В первой строке дано число отрезков. Каждая из последующих n строк содержит по два числа, задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6


Больше всего времени ушло на то, чтобы понять условие. Помог комментарий одного из участников: "есть несколько дощечек разной длины (это наши отрезки n). Нужно прибить их к полу так, чтобы если комната перевернулась они не попадали. Вот минимальное количество гвоздей в этой задаче и точки куда они прибиты и будет решением"


00000000
00001111
01110000
00111100
00000110


00000000
01110000
00111100
00001111
00000110

1 3
2 5
5 6
4 7

'''

import sys
import operator


def get_points(data):
    data = sorted(data[1:], key=operator.itemgetter(1))
    point = data[0][1]
    points = [point]
    for interval in data:
        if interval[0] > point:
            point = interval[1]
            points.append(point)

    print(len(points))
    print(' '.join(map(str, points)))


def main():
    data = []
    for line in sys.stdin:
        item = [int(i) for i in line.split()]
        data.append(item)
    get_points(data)


if __name__ == "__main__":
    main()