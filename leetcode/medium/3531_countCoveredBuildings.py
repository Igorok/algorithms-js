from typing import List
import json
from collections import deque, defaultdict, Counter
import heapq
import math
from functools import cache


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        gridX = {}
        gridY = {}

        for x, y in buildings:
            gridX[x] = gridX.get(x, { 'min': y, 'max': y })
            gridX[x]['min'] = min(gridX[x]['min'], y)
            gridX[x]['max'] = max(gridX[x]['max'], y)

            gridY[y] = gridY.get(y, { 'min': x, 'max': x })
            gridY[y]['min'] = min(gridY[y]['min'], x)
            gridY[y]['max'] = max(gridY[y]['max'], x)

        res = 0
        for x, y in buildings:
            coveredX = gridX[x]['min'] < y and gridX[x]['max'] > y
            coveredY = gridY[y]['min'] < x and gridY[y]['max'] > x

            if coveredX and coveredY:
                res += 1

        return res

'''

[[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]]


5
4 x x
3 x x x
2 x x
1     x
0 1 2 3 4 5 6

gridX 

{2: {'min': 2, 'max': 4}, 1: {'min': 2, 'max': 4}, 3: {'min': 1, 'max': 3}} gridY 
{4: {'min': 1, 'max': 2}, 2: {'min': 1, 'max': 2}, 1: {'min': 3, 'max': 3}, 3: {'min': 1, 'max': 3}}


'''

def test ():
    params = [
        {
            'input': [3, [[1,2],[2,2],[3,2],[2,1],[2,3]]],
            'output': 1,
        },
        {
            'input': [3, [[1,1],[1,2],[2,1],[2,2]]],
            'output': 0,
        },
        {
            'input': [5, [[1,3],[3,2],[3,3],[3,5],[5,3]]],
            'output': 1,
        },
        {
            'input': [4, [[2,4],[1,2],[3,1],[1,4],[2,3],[3,3],[2,2],[1,3]]],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        n, buildings  = param['input']
        result = solution.countCoveredBuildings(n, buildings)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            # msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
