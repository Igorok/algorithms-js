from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        m = len(heaters)
        houses.sort()
        heaters.sort()

        def isOk(radius):
            houseId = 0

            for heaterId in range(m):
                if houses[houseId] + radius < heaters[heaterId]:
                    return False

                left = heaters[heaterId] - radius
                right = heaters[heaterId] + radius
                while houseId < n and (houses[houseId] >= left and houses[houseId] <= right):
                    houseId += 1

                if houseId == n:
                    return True

            return houseId == n

        start = 0
        end = max(houses[-1], heaters[-1])
        res = end - start

        while start <= end:
            middle = (start + end) // 2
            if (isOk(middle)):
                res = middle
                end = middle - 1
            else:
                start = middle + 1

        return res

def test ():
    params = [
        {
            'input': [[1,5], [10]],
            'output': 9,
        },
        {
            'input': [[1,2,3], [2]],
            'output': 1,
        },
        {
            'input': [[1,2,3,4], [1,4]],
            'output': 1,
        },
        {
            'input': [[1,5], [2]],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        houses, heaters = param['input']
        result = solution.findRadius(houses, heaters)
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
