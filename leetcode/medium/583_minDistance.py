from typing import List
import json
from collections import deque

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)
        memo = [[0]*M for i in range(N)]

        for i in range(N):
            for j in range(M):
                top = 0 if i == 0 else memo[i-1][j]
                left = 0 if j == 0 else memo[i][j-1]
                diag = 0 if i == 0 or j == 0 else memo[i-1][j-1]

                memo[i][j] = max(top, left)

                if word1[i] == word2[j]:
                    memo[i][j] = max(memo[i][j], diag + 1)

        common = memo[-1][-1]

        return N-common + M-common

def test ():
    params = [
        {
            'input': ["sea", "eat"],
            'output': 2,
        },
        {
            'input': ["leetcode", "etco"],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        word1, word2 = param['input']
        result = solution.minDistance(word1, word2)
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
