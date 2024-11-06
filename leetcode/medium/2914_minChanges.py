from typing import List
from json import dumps
import heapq

class Solution:
    def minChanges(self, s: str) -> int:
        c0 = 0
        c1 = 0
        res = 0
        i = 1
        for char in s:
            if char == '0':
                c0 += 1
            else:
                c1 += 1
            if (i % 2) == 0 and i > 0:
                res += min(c0, c1)
                c0 = 0
                c1 = 0
            i+= 1

        return res

def test ():
    params = [
        {
            'input': '1001',
            'output': 2,
        },
        {
            'input': '10',
            'output': 1,
        },
        {
            'input': '0000',
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minChanges(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
