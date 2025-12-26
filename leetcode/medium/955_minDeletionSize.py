from typing import List
from collections import deque
from functools import cache
import re

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        memo = [[] for i in range(N)]

        res = 0
        popPrev = False
        for charId in range(M):
            prev = ''
            isWrong = False

            for rowId in range(N):
                if popPrev:
                    memo[rowId].pop()

                memo[rowId].append(strs[rowId][charId])
                curr = ''.join(memo[rowId])

                if prev > curr and not isWrong:
                    res += 1
                    isWrong = True

                prev = curr

            popPrev = isWrong


        return res



def test ():
    params = [
        {
            'input': ["ca","bb","ac"],
            'output': 1,
        },
        {
            'input': ["xc","yb","za"],
            'output': 0,
        },
        {
            'input': ["zyx","wvu","tsr"],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        strs = param['input']
        result = solution.minDeletionSize(strs)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
