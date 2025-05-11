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

        memo = [[-1]*m for i in range(n)]
        memo[0][0] = 0
        memo[1][0] = moveTime[1][0] + 1
        memo[0][1] = moveTime[0][1] + 1

        reachQueue = []
        heapq.heappush(reachQueue, (memo[1][0], 1, 0, 1))
        heapq.heappush(reachQueue, (memo[0][1], 0, 1, 1))

        while reachQueue:
            time, y, x, price = heapq.heappop(reachQueue)

            for sy, sx in shifts:
                ny = sy + y
                nx = sx + x
                if ny < 0 or ny == n or nx < 0 or nx == m:
                    continue

                nPrice = 2 if price == 1 else 1
                nVal = max(time, moveTime[ny][nx]) + nPrice

                if memo[ny][nx] == -1 or memo[ny][nx] > nVal:
                    memo[ny][nx] = nVal
                    if ny != n and nx != m:
                        heapq.heappush(reachQueue, (memo[ny][nx], ny, nx, nPrice))


        return memo[-1][-1]



def test ():
    params = [
        {
            'input': [[0,4],[4,4]],
            'output': 7,
        },
        {
            'input': [[0,0,0,0],[0,0,0,0]],
            'output': 6,
        },
        {
            'input': [[0,1],[1,2]],
            'output': 4,
        },
        {
            'input': [[29,42],[51,59]],
            'output': 61,
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
