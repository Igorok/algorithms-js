'''
Задача на программирование: лестница

Даны число 1 <= n <= 10^2 ступенек лестницы и целые числа -10^4 <= a[1] ,..., a[n] <=10^4 , которыми помечены ступеньки. Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки), каждый раз поднимаясь на одну или две ступеньки.


Sample Input 1:
2
1 2
Sample Output 1:
3

Sample Input 2:
2
2 -1
Sample Output 2:
1

Sample Input 3:
3
-1 2 1
Sample Output 3:
3
'''


'''.git/

Мне помогли вот эти тесты

-2 -16 -13 -9 -48 ответ -63

1 1 -2 -4 -6 2 2 ответ 2

-64 -16 -13 -9 -48 ответ -73
'''

import sys


def get_sum_stairs(n, array):
    sum_stairs = [0] * (n + 1)
    for i in range(1, n + 1):
        prev1 = max(i - 1, 0)
        prev2 = max(i - 2, 0)

        sum1 = array[i - 1] + sum_stairs[prev1]
        sum2 = array[i - 1] + sum_stairs[prev2]
        sum_stairs[i] = max(sum1, sum2)

    return sum_stairs[n]


def main():
    data = []
    for line in sys.stdin:
        data.append([int(i) for i in line.split(' ')])

    sum_stairs = get_sum_stairs(data[0][0], data[1])
    print(sum_stairs)

def test():
    assert get_sum_stairs(2, [1, 2]) == 3
    assert get_sum_stairs(2, [2, -1]) == 1
    assert get_sum_stairs(3, [-1, 2, 1]) == 3


if __name__ == '__main__':
    main()