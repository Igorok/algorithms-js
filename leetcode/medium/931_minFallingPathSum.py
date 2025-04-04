from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        for r in range(1, n):
            for c in range(n):
                value = matrix[r][c] + matrix[r-1][c]
                if c - 1 > -1:
                    value = min(value, matrix[r][c] + matrix[r-1][c-1])
                if c + 1 < n:
                    value = min(value, matrix[r][c] + matrix[r-1][c+1])

                matrix[r][c] = value


        return min(matrix[-1])

'''
[
[2,1,3],
[6,5,4],
[7,8,9]
]



'''

def test ():
    params = [
        {
            'input': [[2,1,3],[6,5,4],[7,8,9]],
            'output': 13,
        },
        {
            'input': [[-19,57],[-40,-5]],
            'output': -59,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minFallingPathSum(param['input'])
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
