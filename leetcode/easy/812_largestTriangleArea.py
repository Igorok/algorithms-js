from typing import List
from json import dumps
import math
import heapq

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def getArea(a, b, c):
            area = 0.5 * abs(a[0]*(b[1] - c[1]) + b[0]*(c[1] - a[1]) + c[0]*(a[1]-b[1]))
            return area

        n = len(points)
        res = -1
        for a in range(n-2):
            for b in range(a+1, n-1):
                for c in range(b+1, n):
                    area = getArea(points[a], points[b], points[c])
                    res = max(res, area)

        return res

def test ():
    params = [
        {
            'input': [[0,0],[0,1],[1,0],[0,2],[2,0]],
            'output': 2.00000,
        },
        {
            'input': [[1,0],[0,0],[0,1]],
            'output': 0.50000,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.largestTriangleArea(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
