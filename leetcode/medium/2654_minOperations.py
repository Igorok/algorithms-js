import json
from collections import deque
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def gcd(a, b):
            while a != 0 and b != 0:
                a, b = (b, a) if a <= b else (a, b)
                a = a % b
            return a if a != 0 else b

        n = len(nums)
        countOfOne = 0
        for i in range(n):
            if nums[i] == 1:
                countOfOne += 1

        if countOfOne > 0:
            return n - countOfOne

        minLength = float("inf")
        for i in range(n):
            acc = nums[i]
            for j in range(i + 1, n):
                acc = gcd(acc, nums[j])
                if acc == 1:
                    minLength = min(minLength, j - i + 1)
                    break

        if minLength == float("inf"):
            return -1

        return (minLength - 1) + n - 1


def test():
    params = [
        {
            "input": [2, 6, 3, 4],
            "output": 4,
        },
        {
            "input": [2, 10, 6, 14],
            "output": -1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minOperations(nums)
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
