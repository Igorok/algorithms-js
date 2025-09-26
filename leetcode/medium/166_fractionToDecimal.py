import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        res = []
        if numerator * denominator < 0:
            res.append('-')
        numerator = abs(numerator)
        denominator = abs(denominator)

        val = numerator // denominator
        res.append(str(val))

        rem = numerator % denominator
        if rem == 0:
            return ''.join(res)

        res.append('.')
        period = defaultdict(int)

        while rem != 0:
            num = rem * 10

            val = ''
            while num < denominator:
                num = num * 10
                val += '0'

            val += str(num // denominator)
            rem = num % denominator
            key = f'{val}_{rem}'

            if key in period:
                res.append(')')
                id = period[key]
                res = res[:id] + ['('] + res[id:]
                break
            else:
                res.append(val)
                period[key] = len(res) - 1

        return ''.join(res)


'''
1/333=0.
1000
333
'''

def test ():
    params = [
        {
            'input': [1, 17],
            'output': "0.(0588235294117647)",
        },
        {
            'input': [1, 333],
            'output': "0.(003)",
        },
        {
            'input': [1, 2],
            'output': "0.5",
        },
        {
            'input': [2, 1],
            'output': "2",
        },
        {
            'input': [4, 333],
            'output': "0.(012)",
        },
        {
            'input': [-1, -2147483648],
            'output': "0.(012)",
        },
    ]
    solution = Solution()

    for param in params:
        numerator, denominator = param['input']
        result = solution.fractionToDecimal(numerator, denominator)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
