from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        N = len(points)
        MOD = 10**9 + 7
        shiftByTg = defaultdict(list)
        tgByDiag = defaultdict(list)


        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                # y = ax + b
                # b = y - ax
                diffY = y1 - y2
                diffX = x1 - x2

                # diffX == 0
                shift = x1
                tg = 'inf'

                if diffX != 0:
                    tg = diffY / diffX
                    # shift = y1 - tg * x1
                    # shift = y1 - (diffY / diffX) * x1
                    # shift = y1 - x1*diffY/diffX
                    # shift = (y1*diffX - x1*diffY)/diffX
                    shift = (y1*diffX - x1*diffY)/diffX

                shiftByTg[tg].append(shift)

                diag = (x1 + x2, y1 + y2)
                tgByDiag[diag].append(tg)


        res = 0


        for tg in shiftByTg:
            if len(shiftByTg[tg]) == 1:
                continue

            countByShift = defaultdict(int)
            for shift in shiftByTg[tg]:
                countByShift[shift] += 1

            prev = 0
            for shift in countByShift:
                cnt = countByShift[shift]
                res += prev * cnt
                prev += cnt


        for diag in tgByDiag:
            if len(tgByDiag[diag]) == 1:
                continue

            # res -= len(tgByDiag[diag]) // 2

            countByTg = defaultdict(int)
            for tg in tgByDiag[diag]:
                countByTg[tg] += 1

            prev = 0
            for tg in countByTg:
                cnt = countByTg[tg]
                res -= prev * cnt
                prev += cnt

        return res

'''

tg(a) = H/L
H = y2 - y1
L = x2 - x1

3
2 - x - x
1
0 x 2 x 4

(1+2, 0+2) = (3,2);
(3+4, 0+2) = (7,2)
(2+4, 2+2) = (6,4)
(1+3, 0+0) = (4,0)

(1+4, 0+2)
(2+3, 2+0)

5
4 - x
3
2 x - x
1
0 1 x 3 4

(1+3, 2+2)
(2+2, 0+4)

'''

def test ():
    params = [
        # {
        #     'input': [[-3,2],[3,0],[2,3],[3,2],[2,-3]],
        #     'output': 2,
        # },
        # {
        #     'input': [[0,0],[1,0],[0,1],[2,1]],
        #     'output': 1,
        # },
        # {
        #     'input': [[1,0], [3,0], [2,2], [4,2]],
        #     'output': 1,
        # },
        {
            'input': [
                [83,-25], [74,11], [-65,-25], [33,-25], [17,-25], [1,30], [-84,-25], [1,-25], [1,-92], [-87,13]
            ],
            'output': 0,
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
