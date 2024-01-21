'''
Задача на программирование: двоичный поиск
В первой строке даны целое число 1 <= n <= 10^5 и массив A[1...n] из n различных натуральных чисел, не превышающих 10^9 , в порядке возрастания,
во второй — целое число 1 <= k <= 10^5 и k натуральных чисел b[1],...,b[k] , не превышающих 10^9. Для каждого i от 1 до k необходимо вывести индекс 1 <= j <= n, для которого A[j] = b[i], или -1, если такого j нет.

Sample Input:
5 1 5 8 12 13
5 8 1 23 1 11

Sample Output:
3 1 -1 1 -1
'''

import sys
import math


def binary_search(_array, _num):
    left = 0
    right = len(_array) - 1
    middle = math.floor((left + right) / 2)

    while left <= right:
        if _array[middle] == _num:
            return middle + 1
        if _array[middle] < _num:
            left = middle + 1
        else:
            right = middle - 1
        middle = math.floor((left + right) / 2)

    return -1


def get_indexes(data):
    ids = []
    for _num in data[1]:
        i = binary_search(data[0], _num)
        ids.append(i)
    return ids


def main():
    data = []
    for line in sys.stdin:
        line = line.split()[1:]
        data.append(list(map(int, line)))

    ids = get_indexes(data)
    print(' '.join(map(str, ids)))


if __name__ == "__main__":
    main()