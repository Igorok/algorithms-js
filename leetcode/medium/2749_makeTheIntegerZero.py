from typing import List
from collections import defaultdict


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        if num1 == num2:
            return 0

        for i in range(1, 33):
            num = num1 - i * num2
            if num < i:
                return -1

            acc = 0
            while num > 0:
                acc += (num & 1)
                num = num >> 1

            if i >= acc:
                return i

        return -1


def test ():
    params = [
        {
            'input': [3, -2],
            'output': 3,
        },
        {
            'input': [5, 7],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        s, dictionary = param['input']

        result = solution.makeTheIntegerZero(s, dictionary)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
