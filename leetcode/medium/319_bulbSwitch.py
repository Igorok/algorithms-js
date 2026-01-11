from typing import List
import heapq
import math
from collections import defaultdict, deque


class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        return 0


'''
1 1 1 1
1 0 1 0
1 0 0 0
1 0 0 1

1 1 1 1 1 1 1 1 1 1 1
1 0 1 0 1 0 1 0 1 0 1
1 0 0 0 1 1 1 0 0 0 1
1 0 0 1 1 1 1 1 0 0 1
1 0 0 1 0 1 1 1 0 1 1
1 0 0 1 0 0 1 1 0 1 1

'''

def test ():
    params = [
        {
            'input': 3,
            'output': 1,
        },
        {
            'input': 0,
            'output': 0,
        },
        {
            'input': 1,
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        s1, s2 = param['input']
        result = solution.minimumDeleteSum(s1, s2)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
