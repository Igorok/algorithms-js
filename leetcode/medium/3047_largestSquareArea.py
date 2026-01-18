from typing import List
import heapq
import math
from collections import defaultdict, deque


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        N = len(bottomLeft)

        res = 0

        for i in range(N):
            for j in range(i+1, N):
                square1 = [bottomLeft[i], topRight[i]]
                square2 = [bottomLeft[j], topRight[j]]

                minXEnd = min(square1[1][0], square2[1][0])
                maxXStart = max(square1[0][0], square2[0][0])
                width = minXEnd - maxXStart

                minYEnd = min(square1[1][1], square2[1][1])
                maxYStart = max(square1[0][1], square2[0][1])
                height = minYEnd - maxYStart

                if width <= 0 or height <= 0:
                    continue

                area = min(height, width) ** 2
                res = max(res, area)

        return res




def test ():
    params = [
        {
            'input': [[[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]]],
            'output': 1,
        },
        {
            'input': [[[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]]],
            'output': 4,
        },
        {
            'input': [ [[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]]],
            'output': 1,
        },
        {
            'input': [ [[1,1],[3,3],[3,1]], [[2,2],[4,4],[4,2]]],
            'output': 0,
        },
        {
            'input': [ [[1,1], [2,2],[3,3]], [[6,6],[5,5],[4,4]]],
            'output': 9,
        },
    ]
    solution = Solution()

    for param in params:
        bottomLeft, topRight = param['input']
        result = solution.largestSquareArea(bottomLeft, topRight)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
