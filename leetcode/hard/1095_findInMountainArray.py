import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class MountainArray:
    def __init__(self, mountainArr):
        self.mountainArr = mountainArr

    def get(self, index: int) -> int:
        return self.mountainArr[index]

    def length(self) -> int:
        return len(self.mountainArr)


class Solution:
    def findInMountainArray(self, target: int, mountainArr) -> int:
        length = mountainArr.length()
        memo = [-1] * length

        def getVal(id):
            if memo[id] != -1:
                return memo[id]
            memo[id] = mountainArr.get(id)
            return memo[id]

        def findLeft():
            start = 0
            end = length - 1
            res = -1

            while start <= end:
                middle = (start + end) // 2
                middleVal = getVal(middle)

                rightVal = -1
                if middle + 1 < length:
                    rightVal = getVal(middle + 1)

                if rightVal < middleVal:
                    if middleVal == target:
                        res = middle

                    end = middle - 1
                    continue

                if middleVal == target:
                    return middle

                if middleVal > target:
                    end = middle - 1
                else:
                    start = middle + 1

            return res

        def findRight():
            start = 0
            end = length - 1
            res = -1

            while start <= end:
                middle = (start + end) // 2
                middleVal = getVal(middle)

                leftVal = -1
                if middle - 1 > -1:
                    leftVal = getVal(middle - 1)

                if leftVal < middleVal:
                    if middleVal == target:
                        res = middle
                    start = middle + 1
                    continue

                if middleVal == target:
                    return middle

                if middleVal > target:
                    start = middle + 1
                else:
                    end = middle - 1

            return res

        r = findLeft()
        if r != -1:
            return r

        return findRight()


def test():
    params = [
        {
            "input": [[1, 2, 3, 4, 5, 3, 1], 3],
            "output": 2,
        },
        {
            "input": [[0, 1, 2, 4, 2, 1], 3],
            "output": -1,
        },
        {
            "input": [[1, 5, 2], 5],
            "output": 1,
        },
        {
            "input": [[3, 5, 3, 2, 0], 2],
            "output": 3,
        },
        {
            "input": [[3, 5, 3, 2, 0], 3],
            "output": 0,
        },
    ]
    solution = Solution()

    for param in params:
        mountainArr, target = param["input"]
        result = solution.findInMountainArray(target, MountainArray(mountainArr))

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
