import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if (x1 <= xCenter <= x2) and (y1 <= yCenter <= y2):
            return True

        r2 = radius**2
        def getDist(x, y):
            l1 = (x-xCenter)**2
            l2 = (y-yCenter)**2
            return l1 + l2 <= r2

        for x in range(x1, x2+1):
            if getDist(x, y1) or getDist(x, y2):
                return True

        for y in range(y1, y2+1):
            if getDist(x1, y) or getDist(x2, y):
                return True



        return False


def test():
    params = [
        {
            "input": [1, 0, 0, 1, -1, 3, 1],
            "output": True,
        },
        {
            "input": [1, 1, 1, 1, -3, 2, -1],
            "output": False,
        },
        {
            "input": [1, 0, 0, -1, 0, 0, 1],
            "output": True,
        },
        {
            "input": [1, 1, 1, -3, -3, 3, 3],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        radius, xCenter, yCenter, x1, y1, x2, y2 = param["input"]
        result = solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)

        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
