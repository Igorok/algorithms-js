'''
Задача на программирование: точки и отрезки

В первой строке задано два целых числа 1 <= n <= 50000 и 1 <= m <= 50000 — количество отрезков и точек на прямой, соответственно. Следующие n строк содержат по два целых числа a[i] и b[i] (a[i] <= b[i]) — координаты концов отрезков. Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю. Точка считается принадлежащей отрезку, если она находится внутри него или на границе. Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Sample Input:
2 3
0 5
7 10
1 6 11

Sample Output:
1 0 0
'''

'''
Решение отсортировать начало и конец
найти сколько нужные начала
вычесть из них закончившиеся отрезки
'''

'''.git/

У кого крякнулся тест #6 (  Failed test #6. Wrong answer )
Попробуйте:
6 9
0 0
-1 1
-2 2
-3 3
-4 4
-5 5
-5 -4 -3 -1 0 1 3 4 5

Нужно получить 1 2 3 5 6 5 3 2 1


1 2 3 5 6 0 0 0 0

'''

import sys
import random


def quick_sort(array):
    array_len = len(array)
    if array_len < 2:
        return array

    idx = random.randint(0, array_len - 1)

    left = []
    right = []
    middle = []

    for i in range(array_len):
        if array[i] < array[idx]:
            left.append(array[i])
        elif array[i] > array[idx]:
            right.append(array[i])
        else:
            middle.append(array[i])

    left = quick_sort(left)
    right = quick_sort(right)

    return left + middle + right


def search_less_or_equal(array, query_num):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2

    if array[left] > query_num:
        return 0

    if array[right] <= query_num:
        return right + 1

    while left < right:
        if array[middle] <= query_num:
            if middle + 1 <= right and array[middle + 1] > query_num:
                return middle + 1
            left = middle + 1
        else:
            if middle - 1 >= 0 and array[middle - 1] <= query_num:
                return middle
            right = middle - 1
        middle = (left + right) // 2

    return left + 1


def search_less(array, query_num):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2

    if array[left] >= query_num:
        return 0

    if array[right] < query_num:
        return right + 1

    while left < right:
        if array[middle] < query_num:
            if middle + 1 <= right and array[middle + 1] >= query_num:
                return middle + 1
            left = middle + 1
        else:
            if middle - 1 >= 0 and array[middle - 1] < query_num:
                return middle
            right = middle - 1
        middle = (left + right) // 2

    return left + 1


def main():
    data = []
    for line in sys.stdin:
        data.append([int(val) for val in line.split(' ')])

    points = data.pop()
    start_interval = []
    end_interval = []

    for i in range(1, len(data)):
        start_interval.append(data[i][0])
        end_interval.append(data[i][1])

    start_interval = quick_sort(start_interval)
    end_interval = quick_sort(end_interval)

    for i in range(len(points)):
        started = search_less_or_equal(start_interval, points[i])
        ended = search_less(end_interval, points[i])
        points[i] = str(0 if started < ended else started - ended)

    print(' '.join(points))

if __name__ == '__main__':
    main()