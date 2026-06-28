import json

# from functools import cache
import math
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ones = 0
        res = 1

        countOfNums = Counter(nums)
        visited = set()

        for num in nums:
            if num == 1:
                ones += 1
                continue

            if num in visited:
                continue

            n = num
            r = 1

            while n**2 in countOfNums:
                if countOfNums[n] == 1:
                    break

                r += 1
                n = n**2
                visited.add(n)

            res = max(res, r * 2 - 1)

        ones = ones if ones % 2 == 1 else ones - 1
        return max(res, ones)


def test():
    params = [
        {
            "input": [5, 4, 1, 2, 2],
            "output": 3,
        },
        {
            "input": [1, 3, 2, 4],
            "output": 1,
        },
        {
            "input": [1, 1],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.maximumLength(nums)
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
