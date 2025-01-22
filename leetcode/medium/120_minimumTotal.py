from typing import List
from json import dumps
from collections import deque

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        arr = [triangle[0]]

        for i in range(1, len(triangle)):
            arr.append([0] * (i + 1))
            for j in range(i + 1):
                left = float('inf')
                if j - 1 >= 0:
                    left = arr[i-1][j-1]
                if j < i:
                    right = arr[i-1][j]
                arr[i][j] = triangle[i][j] + int(min(left, right))

        return min(arr[-1])

def test ():
    params = [
        {
            'input': [[2],[3,4],[6,5,7],[4,1,8,3]],
            'output': 11,
        },
        {
            'input': [[-10]],
            'output': -10,
        },
        {
            'input': [
                [-1],
                [2,3],
                [1,-1,-3]
            ],
            'output': -1,
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.minimumTotal(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
