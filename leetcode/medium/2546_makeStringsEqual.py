from typing import List
from json import dumps
from collections import deque


class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        z1 = 0
        o1 = 0
        for char in s:
            z1 += 1 if char == '0' else 0
            o1 += 1 if char == '1' else 0

        z2 = 0
        o2 = 0
        for char in target:
            z2 += 1 if char == '0' else 0
            o2 += 1 if char == '1' else 0


        if o2 == 0 and o1 > 0:
            return False

        if o2 > 0 and o1 == 0:
            return False


        return True



def test ():
    params = [
        {
            'input': ["1010", "0110"],
            'output': True,
        },
        {
            'input': ["11", "00"],
            'output': False,
        },
        {

            'input': ["010101", "111111"],
            'output': True,
        },
        {
            'input': ["0000", "1111"],
            'output': False,
        },
        {
            'input': ["00", "10"],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:

        s, target = param['input']
        result = solution.makeStringsEqual(s, target)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
