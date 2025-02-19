from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 1

        for i in range(len(points)):
            aCount = {}
            equalXCount = {}

            for j in range(i+1, len(points)):
                xd = points[i][0] - points[j][0]
                if xd == 0:
                    xCount = equalXCount.get(points[i][0], 1)
                    xCount += 1
                    equalXCount[points[i][0]] = xCount
                    res = max(res, equalXCount[points[i][0]])
                    continue

                yd = points[i][1] - points[j][1]
                a = yd / xd
                ac = aCount.get(a, 1)
                ac += 1
                aCount[a] = ac
                res = max(res, aCount[a])

        return res

'''

[4,1],[3,2],[2,3],[1,4]

y = a*x + b
y1 - y2 = a*x1 - a*x2 + b - b = a(x1 - x2)
dY = a*dX
a = dY/dX


(1, 5)
(1, 2)
(1, 3)
(1, 4)

'''

def test ():
    params = [
        {
            'input': [[1,1],[2,2],[3,3]],
            'output': 3,
        },
        {
            'input': [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        points = param['input']
        result = solution.maxPoints(points)
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
