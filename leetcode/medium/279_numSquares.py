from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def numSquares_0(self, n: int) -> int:
        num =  n
        res = 0
        while num != 0:
            val = int(num ** (0.5))
            val *= val
            res += 1
            num -= val

        return res

    def numSquares(self, n: int) -> int:
        if n < 4:
            return n

        squares = [1]
        for i in range(2, 101):
            squares.append(i**2)

        prev = [i for i in range(n+1)]
        res = prev[n]
        for i in range(1, 100):
            num = squares[i]
            if num > n:
                break

            curr = prev.copy()
            for j in range(num, n+1):
                if j == num:
                    curr[num] = 1
                    continue

                diff = j - num
                curr[j] = min(curr[j], curr[diff]+1)
            prev = curr

            res = min(res, curr[n])



        return res

'''
4
9
16 = 4+4+4+4
25 = 16+9 = 4+4+4+4+9
36 = 4*9
49 = 45+4 = 9+9+9+9+9+4
11 = 9+1+1

10000
9999

'''

def test ():
    params = [
        {
            'input': 12,
            'output': 3,
        },
        {
            'input': 13,
            'output': 2,
        },
        {
            'input': 25,
            'output': 1,
        },
        {
            'input': 11,
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.numSquares(nums)
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
