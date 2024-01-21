'''
Задача на программирование: число инверсий
Первая строка содержит число 1 <= n <= 10^5 , вторая — массив A[1...n], содержащий натуральные числа, не превосходящие 10^9 . Необходимо посчитать число пар индексов 1 <= i < j <= n, для которых A[i] > A[j]. (Такая пара элементов называется инверсией массива. Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности: например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)

Sample Input:
5
2 3 9 2 9

Sample Output:
2
'''

import sys
import math


class InvariationManager:
    invariation = 0

    def __init__(self, array):
        self.array = array

    def merge_sort(self, array):
        arr_len = len(array)
        if arr_len < 2:
            return array

        middle = arr_len // 2
        right_len = arr_len - middle
        left = self.merge_sort(array[:middle])
        right = self.merge_sort(array[middle:])

        merged = []
        i = 0
        j = 0
        while i < middle or j < right_len:
            if j == right_len or (i < middle and left[i] <= right[j]):
                merged.append(left[i])
                i += 1
            else:
                self.invariation += middle - i
                merged.append(right[j])
                j += 1

        return merged


    def get_count(self):
        sorted_array = self.merge_sort(self.array)
        return self.invariation


def main():
    data = []
    for line in sys.stdin:
        data.append([int(val) for val in line.split(' ')])

    invariationManager = InvariationManager(data[1])
    count = invariationManager.get_count()

    print(str(count))


if __name__ == "__main__":
    main()