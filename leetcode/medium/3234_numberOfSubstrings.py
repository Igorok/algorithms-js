from typing import List
import json
from collections import deque, defaultdict
import math


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        nextZeros = [N]*N
        for i in range(N-2, -1 ,- 1):
            nextZeros[i] = i+1 if s[i+1] == '0' else nextZeros[i+1]

        res = 0

        for left in range(N):
            zeros = 1 if s[left] == '0' else 0
            middle = left

            while (zeros**2) <= N:
                right = nextZeros[middle]
                length = right - left
                part = right - middle
                ones = length - zeros
                diff = ones - zeros**2

                if diff >= 0:
                    res += min(diff + 1, part)

                zeros += 1
                middle = right
                if middle == N:
                    break


        return res

'''
0011011

101011

101101
1+3+1=4
0+



'''


def test ():
    params = [
        {
            'input': '00011',
            'output': 5,
        },
        {
            'input': '101101',
            'output': 16,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.numberOfSubstrings(s)
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
