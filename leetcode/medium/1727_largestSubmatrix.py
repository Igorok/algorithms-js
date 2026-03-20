from typing import List
from json import dumps
from collections import deque
import heapq

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        M = len(matrix[0])
        res = 0

        for row in range(N):
            if row > 0:
                for col in range(M):
                    if matrix[row][col] == 0:
                        continue
                    matrix[row][col] += matrix[row-1][col]

            arr = matrix[row].copy()
            arr.sort()

            for i in range(M):
                if arr[i] == 0:
                    continue
                area = arr[i] * (M-i)
                res = max(res, area)

        return res

'''

[
[1,0,1,0,1],
[1,0,1,0,1],
[1,0,0,1,0],
[0,1,0,1,0],
[0,1,0,0,0],
[0,1,0,0,0],
]
3,3,2,2,2


[
[1,0,1,0,1],
[2,0,2,0,2],
[3,0,0,1,0],
[0,1,0,2,0],
[0,2,0,0,0],
[0,3,0,0,0],
]




JSON.stringify([
[1,0,1,0,1],
[1,0,1,0,1],
[1,0,0,1,0],
[0,1,0,1,0],
[0,1,0,0,0],
[0,1,0,0,0],
])




[
[1, 0, 1, 0, 1],
[2, 0, 2, 0, 2],
[3, 0, 0, 1, 0],
[0, 1, 0, 2, 0],
[0, 2, 0, 0, 0],
[0, 3, 0, 0, 0]
]


1,2,3,4,5

'''


def test ():
    params = [
        {
            'input': [[0,0,1],[1,1,1],[1,0,1]],
            'output': 4,
        },
        {
            'input': [[1,0,1,0,1]],
            'output': 3,
        },
        {
            'input': [[1,1,0],[1,0,1]],
            'output': 2,
        },
        {
            'input': [[1,1,0],[1,0,1],[0,1,1]],
            'output': 2,
        },
        {
            'input': [[1,0,1,0,1],[1,0,1,0,1],[1,0,0,1,0],[0,1,0,1,0],[0,1,0,0,0],[0,1,0,0,0]],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        matrix = param['input']
        result = solution.largestSubmatrix(matrix)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
