import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 7 + 10**9
        hFences = hFences + [1, m]
        hFences.sort()

        vFences = vFences + [1, n]
        vFences.sort()

        yLengths = set()
        for id in range(1, len(hFences)):
            for i in range(id):
                yLengths.add(hFences[id] - hFences[i])

        length = 0
        res = -1
        for id in range(1, len(vFences)):
            for i in range(id):
                xLength = vFences[id] - vFences[i]
                if xLength in yLengths and xLength > length:
                    length = xLength
                    res = (length**2) % MOD

        return res

'''
"input": [6, 4, [3], [3,2]],

1 2 3 4 5
2 | | |
3 + + | -
4 | | |
5 | | |
6 - - - -
7



'''



def test():
    params = [
        {
            "input": [4, 3, [2,3], [2]],
            "output": 4,
        },
        {
            "input": [6, 7, [2], [4]],
            "output": -1,
        },
        {
            "input": [6, 4, [3], [3,2]],
            "output": 9,
        },
    ]
    solution = Solution()

    for param in params:
        m, n, hFences, vFences = param["input"]
        result = solution.maximizeSquareArea(m, n, hFences, vFences)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
