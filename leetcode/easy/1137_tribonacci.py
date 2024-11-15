from typing import List
from json import dumps
import heapq

class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0, 1, 1]
        if n < 3:
            return res[n]

        for i in range(3, n + 1):
            res[0], res[1], res[2] = res[1], res[2], (res[0] + res[1] + res[2])

        return res[2]

def test ():
    params = [
        {
            'input': 3,
            'output': 2,
        },
        {
            'input': 4,
            'output': 4,
        },
        {
            'input': 25,
            'output': 1389537,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.tribonacci(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
