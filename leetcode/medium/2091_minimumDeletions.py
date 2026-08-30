import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 3:
            return N

        minId = 0
        maxId = 0
        for i in range(1, N):
            if nums[i] > nums[maxId]:
                maxId = i
            if nums[i] < nums[minId]:
                minId = i

        left, right = [minId, maxId] if minId < maxId else [maxId, minId]

        afterLeft = right + 1
        afterRight = N - left
        afterBoth = left + 1 + N - right


        return min(afterLeft, afterRight, afterBoth)


def test():
    params = [
        {
            "input": [2,10,7,5,4,1,8,6],
            "output": 5,
        },
        {
            "input": [0,-4,19,1,8,-2,-3,5],
            "output": 3,
        },
        {
            "input": [101],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minimumDeletions(nums)

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
