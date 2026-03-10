from typing import List
from json import dumps

class Solution:
    def minOperations(self, s: str) -> int:
        N = len(s)

        r1 = 0
        r2 = 0

        for i in range(0, N, 2):
            # 01 way
            if s[i] != '0':
                r1 += 1
            if i + 1 < N:
                if s[i+1] != '1':
                    r1 += 1

            # 10 way
            if s[i] != '1':
                r2 += 1
            if i + 1 < N:
                if s[i+1] != '0':
                    r2 += 1

        return min(r1, r2)

'''

0000101011010101010101010101
010101010

'''

def test ():
    params = [
        {
            'input': '0100',
            'output': 1,
        },
        {
            'input': '10',
            'output': 0,
        },
        {
            'input': '1111',
            'output': 2,
        },
        {
            'input': '1010000',
            'output': 2,
        },
        {
            'input': '0000101010101',
            'output': 2,
        },
        {
            'input': '0000101011010101010101010101',
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minOperations(s)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
