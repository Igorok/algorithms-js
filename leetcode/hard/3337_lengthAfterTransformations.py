from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

'''

1 2
3 4
5 6

1 2 3
4 5 6

1*1+2*4    1*2+2*5    1*3+2*6
3*1+4*4    3*2+4*5    3*3+4*6
5*1+6*4    5*2+6*5    5*3+6*6

9   12  15
19  26  33
29  40  51


2**5
4**2 * 2**1
16**1 * 2

'''


class Solution:
    mod = 7+10**9

    def multiplyMatrix(self, m1, m2):
        res = [[0]*26 for i in range(26)]

        for i in range(26):
            for j in range(26):
                for k in range(26):
                    res[i][j] += (m1[i][k] * m2[k][j]) % self.mod
                    res[i][j] %= self.mod

        return res

    def powMatrix(self, matrix, degree):
        res = [[0]*26 for i in range(26)]
        for i in range(26):
            res[i][i] = 1

        while degree > 0:
            if degree & 1:
                res = self.multiplyMatrix(res, matrix)

            matrix = self.multiplyMatrix(matrix, matrix)
            degree = degree >> 1

        return res

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        charsCount = [0]*26
        aCode = ord('a')
        for char in s:
            charsCount[ord(char) - aCode] += 1

        multiMatrix = [[0]*26 for i in range(26)]
        for i in range(26):
            for j in range(i+1, i + nums[i] + 1):
                multiMatrix[j % 26][i] += 1

        multiMatrix = self.powMatrix(multiMatrix, t)

        resCount = [0]*26
        for i in range(26):
            for j in range(26):
                resCount[i] += (charsCount[i] * multiMatrix[j][i]) % self.mod
                resCount[i] %= self.mod

        res = 0
        for num in resCount:
            res += num
            res %= self.mod

        return int(res)


def test ():
    params = [
        {
            'input': ["mppgvcssluzhipednraxbdfbyn", 3719, [5,3,8,1,4,2,2,4,5,2,8,5,8,2,6,10,8,1,4,1,7,4,2,4,7,5]],
            'output': 467065288,
        },
        {
            'input': ["abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]],
            'output': 7,
        },
        {
            'input': ["azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]],
            'output': 8,
        },
    ]
    solution = Solution()

    for param in params:
        s, t, nums = param['input']
        result = solution.lengthAfterTransformations(s, t, nums)
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
