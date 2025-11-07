from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        sweeped = [0] * (n+1)
        minPossible = stations[0]
        maxPossible = 0

        for i in range(n):
            minPossible = min(minPossible, stations[i])
            maxPossible += stations[i]

            left = max(0, i - r)
            right = min(n, i + r + 1)
            sweeped[left] += stations[i]
            sweeped[right] -= stations[i]

        maxPossible += k

        def isOk(minPower):
            acc = 0
            limit = k
            powers = sweeped.copy()

            for i in range(n):
                acc += powers[i]
                if acc >= minPower:
                    continue

                diff = minPower - acc
                if diff > limit:
                    return False

                limit -= diff
                powers[i] += diff
                acc += diff
                right = min(n, i + 2*r + 1)
                powers[right] -= diff



            return True

        res = minPossible

        while minPossible <= maxPossible:
            middle = (minPossible + maxPossible) // 2

            if isOk(middle):
                res = middle
                minPossible = middle + 1
            else:
                maxPossible = middle - 1



        return res

'''
'input': [[1,2,4,5,0], 1, 2],
'output': 5,

1, 2, 4, 5, 0
3  7  11 9  5

3  2  4  5  0
5  9  11 9  5


'''




def test ():
    params = [
        {
            'input': [[1,2,4,5,0], 1, 2],
            'output': 5,
        },
        {
            'input': [[4,4,4,4], 0, 3],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        stations, r, k = param['input']
        result = solution.maxPower(stations, r, k)
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
