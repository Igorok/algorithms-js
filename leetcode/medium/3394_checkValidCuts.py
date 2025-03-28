from typing import List
import json
from collections import deque, defaultdict
import heapq


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xLoc = []
        yLoc = []

        for x1, y1, x2, y2 in rectangles:
            xLoc.append([x1, x2])
            yLoc.append([y1, y2])

        def checkCuts(arr):
            arr.sort()
            lines = 0

            prev = arr[0]
            for i in range(1, len(arr)):
                s, e = arr[i]

                if s >= prev[0] and s < prev[1]:
                    prev[1] = max(prev[1], e)
                    continue

                if s >= prev[1]:
                    prev = [s, e]
                    lines += 1
                    if lines == 2:
                        return True

            return False

        if checkCuts(xLoc):
            return True
        if checkCuts(yLoc):
            return True

        return False

'''

(0,6) (1,2) (1,3) (1,4) (2,3)


'''


def test ():
    params = [
        {
            'input': [5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]],
            'output': True,
        },
        {
            'input': [4, [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]],
            'output': True,
        },
        {
            'input': [4, [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        n, rectangles = param['input']
        result = solution.checkValidCuts(n, rectangles)
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
