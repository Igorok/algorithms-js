from typing import List
import json
from collections import deque, defaultdict
import math
import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        shifts = ((1, 0), (-1, 0), (0, 1), (0, -1))
        n = len(moveTime)
        m = len(moveTime[0])
        minTimes = [[-1]*m for i in range(n)]
        minTimes[0][0] = 0


        cellQueue = [(0, 0, 0)]

        while cellQueue:
            acc, i, j = heapq.heappop(cellQueue)
            for shiftY, shiftX in shifts:
                newY = i + shiftY
                newX = j + shiftX
                if newY < 0 or newY == n or newX < 0 or newX == m:
                    continue
                newTime = max(moveTime[newY][newX], acc) + 1
                if minTimes[newY][newX] == -1 or minTimes[newY][newX] > newTime:
                    minTimes[newY][newX] = newTime
                    heapq.heappush(cellQueue, (newTime, newY, newX))



        return minTimes[-1][-1]

'''

[0,1],
[1,2]

0 2
2 3

'''

def test ():
    params = [
        {
            'input': [[0,4],[4,4]],
            'output': 6,
        },
        {
            'input': [[0,0,0],[0,0,0]],
            'output': 3,
        },
        {
            'input': [[0,1],[1,2]],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        moveTime = param['input']
        result = solution.minTimeToReach(moveTime)
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
