from typing import List
import json
from collections import deque
import heapq
import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 7 + 10**9
        heights = {}

        for x, y in points:
            heights[y] = heights.get(y, [0,0])
            if heights[y][0] == 0:
                heights[y][0] = 1
            else:
                heights[y][1] += heights[y][0]
                heights[y][0] += 1

        res = 0
        lines = 0
        for y in heights.keys():
            res = ((heights[y][1] * lines) % MOD + res) % MOD
            lines += heights[y][1]

        return res

'''
[1,0],[2,0],[3,0],[2,2],[3,2]

4
3
2 - x x
1
0 x x x 4

'''

def test ():
    params = [
        {
            'input': [[1,0],[2,0],[3,0],[2,2],[3,2]],
            'output': 3,
        },
        {
            'input': [[0,0],[1,0],[0,1],[2,1]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        points = param['input']
        result = solution.countTrapezoids(points)
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
