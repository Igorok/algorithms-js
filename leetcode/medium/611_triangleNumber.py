import sys

sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution_0:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        def getId(num, _start):
            start = _start
            end = n - 1
            res = -1

            while start <= end:
                middle = (start + end) // 2
                if nums[middle] < num:
                    res = middle
                    start = middle + 1
                else:
                    end = middle - 1

            return res

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                maxLength = nums[i] + nums[j]
                id = getId(maxLength, j + 1)
                if id != -1:
                    res += id - j

        return res


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        def getId(num, _start):
            start = _start
            end = n - 1
            res = -1

            while start <= end:
                middle = (start + end) // 2
                if nums[middle] < num:
                    res = middle
                    start = middle + 1
                else:
                    end = middle - 1

            return res

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                maxLength = nums[i] + nums[j]
                id = getId(maxLength, j + 1)
                if id != -1:
                    res += id - j

        return res


def test():
    params = [
        {
            "input": [2, 2, 3, 4],
            "output": 3,
        },
        {
            "input": [4, 2, 3, 4],
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.triangleNumber(param["input"])
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
