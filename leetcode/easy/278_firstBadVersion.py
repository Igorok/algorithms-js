from typing import List
from json import dumps


class Solution:
    def __init__(self, bad):
        self.bad = bad

    def isBadVersion(self, n: int):
        return n >= self.bad

    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n

        while start <= end:
            middle = (start + end) // 2

            if self.isBadVersion(middle):
                if self.isBadVersion(middle - 1):
                    end = middle - 1
                else:
                    return middle
            else:
                if self.isBadVersion(middle + 1):
                    return middle + 1
                else:
                    start = middle + 1


def test ():
    params = [
        {
            'input': [5,4],
            'output': 4,
        },
        {
            'input': [1,1],
            'output': 1,
        },
    ]

    for param in params:
        n, bad = param['input']
        solution = Solution(bad)

        result = solution.firstBadVersion(n)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
