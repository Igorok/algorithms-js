from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        def dfs(s):
            left = 0
            cnt = 0
            res = 0

            for right in range(len(s)):
                cnt += 1 if s[right] == '(' else -1

                if cnt == 0:
                    if right + 1 - left == 2:
                        res += 1
                    else:
                        res += 2 * dfs(s[left+1: right])
                    left = right + 1

            return res

        return dfs(s)


def test ():
    params = [
        {
            'input': "()",
            'output': 1,
        },
        {
            'input': "(())",
            'output': 2,
        },
        {
            'input': "()()",
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.scoreOfParentheses(s)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
