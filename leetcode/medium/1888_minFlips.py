from typing import List
from json import dumps
from collections import deque


class Solution:
    def minFlips(self, s: str) -> int:
        N = len(s)
        M = N*2

        s = s+s
        target1 = ''
        target2 = ''

        for i in range(M):
            if i % 2 == 0:
                target1 += '0'
                target2 += '1'
            else:
                target1 += '1'
                target2 += '0'

        # print('target1', target1)
        # print('target2', target2)

        res = M

        diff1 = 0
        diff2 = 0

        left = 0
        for right in range(M):
            if s[right] != target1[right]:
                diff1 += 1
            if s[right] != target2[right]:
                diff2 += 1

            if right >= N:
                if s[left] != target1[left]:
                    diff1 -= 1
                if s[left] != target2[left]:
                    diff2 -= 1
                left += 1

            if right + 1 - left == N:
                res = min(res, diff1, diff2)






        return res



def test ():
    params = [
        {
            'input': '111000',
            'output': 2,
        },
        {
            'input': '010',
            'output': 0,
        },
        {
            'input': '1110',
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.minFlips(s)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
