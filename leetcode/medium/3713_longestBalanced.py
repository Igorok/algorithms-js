from typing import List
from collections import deque, defaultdict
from functools import cache
import re

class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        res = 0

        for i in range(N):
            if res > N-i:
                break

            charsCnt = {}
            freqCnt = {}
            for j in range(i, N):
                cnt = charsCnt.get(s[j], 0) + 1
                charsCnt[s[j]] = cnt

                frq = freqCnt.get(cnt, 0) + 1
                freqCnt[cnt] = frq
                if (cnt-1) in freqCnt:
                    freqCnt[cnt-1] -= 1
                    if freqCnt[cnt-1] == 0:
                        del freqCnt[cnt-1]

                if len(freqCnt) == 1:
                    res = max(res, j-i+1)

        return res

'''

aabcdbcd

'''

def test ():
    params = [
        {
            'input': 'abbac',
            'output': 4,
        },
        {
            'input': 'zzabccy',
            'output': 4,
        },
        {
            'input': 'aba',
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.longestBalanced(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
