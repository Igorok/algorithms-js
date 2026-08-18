
from typing import List
import json
from collections import deque, defaultdict
from functools import cache

'''
There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.
'''

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        N = len(stoneValue)
        sumOfValues = [0]*N
        sumOfValues[0] = stoneValue[0]
        for i in range(1, N):
            sumOfValues[i] = sumOfValues[i-1] + stoneValue[i]

        # print('sumOfValues', sumOfValues)

        memo = [[-1]*(N+1) for i in range(N+1)]

        def rec(start, end):
            if start >= end:
                return 0

            if memo[start][end] != -1:
                return memo[start][end]

            res = -1
            for i in range(start, end):
                prev = 0 if start == 0 else sumOfValues[start-1]
                left = sumOfValues[i] - prev
                right = sumOfValues[end] - sumOfValues[i]

                curr = 0

                if left < right:
                    curr = left
                    r = rec(start, i)
                    curr += r
                elif  right < left:
                    curr = right
                    r = rec(i+1, end)
                    curr += r
                else:
                    curr = left
                    r1 = rec(start, i)
                    r2 = rec(i+1, end)
                    curr += max(r1, r2)

                res = max(res, curr)

            memo[start][end] = res

            return res


        return rec(0, N-1)


def test ():
    params = [
        {
            'input': [6,2,3,4,5,5],
            'output': 18,
        },
        {
            'input': [7,7,7,7,7,7,7],
            'output': 28,
        },
        {
            'input': [4],
            'output': 0,
        },
        {
            'input': [2,3],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        stoneValue = param['input']
        result = solution.stoneGameV(stoneValue)
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
