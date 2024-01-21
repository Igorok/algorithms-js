'''
Задача на программирование: сортировка подсчётом

Первая строка содержит число 1 <= n <= 10^4 , вторая - n натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.

Sample Input:
5
2 3 9 2 9

Sample Output:
2 2 3 9 9
'''

import sys


def get_sorted_numbers(array_numbers):
    len_numbers = len(array_numbers)
    counter_numbers = [0] * 11
    sorted_numbers = [None] * len_numbers

    for i in range(len_numbers):
        counter_numbers[array_numbers[i]] += 1

    for i in range(1, 11):
        counter_numbers[i] += counter_numbers[i - 1]

    for i in reversed(range(len_numbers)):
        idx = counter_numbers[array_numbers[i]]
        sorted_numbers[idx - 1] = array_numbers[i]
        counter_numbers[array_numbers[i]] -= 1

    return sorted_numbers


def main():
    data = []
    for line in sys.stdin:
        data.append([int(val) for val in line.split(' ')])

    sorted_numbers = get_sorted_numbers(data[1])

    print(' '.join(map(str, sorted_numbers)))


if __name__ == '__main__':
    main()
