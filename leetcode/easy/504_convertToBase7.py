from collections import deque
from typing import List
from json import dumps

class Solution:
    def convertToBase7(self, num: int) -> str:
        pref = '' if num > 0 else '-'
        res = ''
        num = abs(num)
        while num != 0:
            res += str(num % 7)
            num = num // 7

        return pref + res[::-1]

def test ():
    params = [
        {
            'input': 100,
            'output': 202,
        },
        {
            'input': -7,
            'output': -10,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.convertToBase7(param['input'])

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
