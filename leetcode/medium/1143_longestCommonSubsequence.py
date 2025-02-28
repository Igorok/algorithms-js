from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        memo = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                maxTop = 0 if i == 0 else memo[i-1][j]
                maxLeft = 0 if j == 0 else memo[i][j-1]
                maxPrev = 0 if (i == 0 or j == 0) else memo[i-1][j-1]

                if text1[i] == text2[j]:
                    maxPrev += 1

                memo[i][j] = max(maxTop, maxLeft, maxPrev)

        return memo[-1][-1]


'''
  a b c d e
a 1 1 1 1 1
c 1 1 2 2 2
e 1 1 2 2 3

'''


def test ():
    params = [
        {
            'input': ["abcde", "ace"],
            'output': 3,
        },
        {
            'input': ["abc", "abc"],
            'output': 3,
        },
        {
            'input': ["abc", "def"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        str1, str2 = param['input']
        result = solution.longestCommonSubsequence(str1, str2)
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
