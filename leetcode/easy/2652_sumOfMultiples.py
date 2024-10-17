from typing import List
from json import dumps


class Solution:
    def sumOfMultiples(self, n: int) -> int:
        s = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                s += i

        return s


def test ():
    params = [
        {
            'input': 7,
            'output': 21,
        },
        {
            'input': 10,
            'output': 40,
        },
        {
            'input': 9,
            'output': 30,
        },
    ]

    solution = Solution()
    for param in params:
        result = solution.sumOfMultiples(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
