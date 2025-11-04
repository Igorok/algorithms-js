from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        left = 0
        maxVal = float('-inf')
        sumVal = 0
        res = 0

        for right in range(n):
            if colors[right] == colors[left]:
                maxVal = max(maxVal, neededTime[right])
                sumVal += neededTime[right]
            else:
                if right - left > 1:
                    res += sumVal - maxVal

                maxVal = neededTime[right]
                sumVal = neededTime[right]
                left = right

        if n - left > 1:
            res += sumVal - maxVal

        return res

def test ():
    params = [
        {
            'input': ["abaac", [1,2,3,4,5]],
            'output': 3,
        },
        {
            'input': ["abc", [1,2,3]],
            'output': 0,
        },
        {
            'input': ["aabaa", [1,2,3,4,1]],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        colors, neededTime = param['input']
        result = solution.minCost(colors, neededTime)
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
