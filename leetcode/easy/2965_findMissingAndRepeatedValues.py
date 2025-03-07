from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [0, 0]
        memo = [0]*(n*n+1)

        for i in range(n):
            for num in grid[i]:
                memo[num] += 1

        for i in range(len(memo)):
            if memo[i] == 2:
                res[0] = i
            if memo[i] == 0:
                res[1] = i

        return res

def test ():
    params = [
        {
            'input': [[1,3],[2,2]],
            'output': [2,4],
        },
        {
            'input': [[9,1,7],[8,9,2],[3,4,6]],
            'output': [9,5],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.findMissingAndRepeatedValues(param['input'])
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
