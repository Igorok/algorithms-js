from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def lcs(self, str1, str2):
        n = len(str1)
        m = len(str2)
        memo = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                top = 0 if i == 0 else memo[i-1][j]
                left = 0 if j == 0 else memo[i][j-1]
                prev = 0 if i == 0 or j == 0 else memo[i-1][j-1]
                if str1[i] == str2[j]:
                    prev += 1
                memo[i][j] = max(top, left, prev)

        subs = []
        i = n-1
        j = m-1
        while i > -1 and j > -1:
            if str1[i] == str2[j]:
                subs.append(str1[i])
                i -= 1
                j -= 1
                continue

            if (i > 0 and memo[i-1][j] > memo[i][j-1] or j == 0):
                i -= 1
            else:
                j -= 1

        subs.reverse()
        return ''.join(subs)

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        n = len(str1)
        m = len(str2)
        lcs = self.lcs(str1, str2)

        res = ''

        i1 = 0
        i2 = 0
        for char in lcs:
            while i1 < n and str1[i1] != char:
                res += str1[i1]
                i1 += 1
            while i2 < m and str2[i2] != char:
                res += str2[i2]
                i2 += 1

            i1 += 1
            i2 += 1
            res += char

        while i1 < n:
            res += str1[i1]
            i1 += 1
        while i2 < m:
            res += str2[i2]
            i2 += 1

        return res




def test ():
    params = [
        {
            'input': ["bcacaaab", "bbabaccc"],
            'output': 'bcbacaaabaccc',
        },
        {
            'input': ["bbbaaaba", "bbababbb"],
            'output': 'bbbaaababbb',
        },
        {
            'input': ["abac", "cab"],
            'output': 'cabac',
        },
        {
            'input': ["aaaaaaaa", "aaaaaaaa"],
            'output': 'aaaaaaaa',
        },
    ]
    solution = Solution()

    for param in params:
        str1, str2 = param['input']
        result = solution.shortestCommonSupersequence(str1, str2)
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
