import json
from collections import deque
from functools import cache
from typing import List


class Solution_0:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = -1
        evenPossible = True
        oddPossible = True

        nums1.sort()

        for num in nums1:
            if (num % 2) == 1:
                if odd == -1:
                    evenPossible = False
                odd = num
            else:
                if odd == -1:
                    oddPossible = False

            if not evenPossible and not oddPossible:
                return False

        return evenPossible or oddPossible


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float("inf")
        minEven = float("inf")
        for num in nums1:
            if (num % 2) == 1:
                minOdd = min(minOdd, num)
            else:
                minEven = min(minEven, num)

        if minOdd == float("inf") or minEven == float("inf"):
            return True

        return minEven > minOdd


def test():
    params = [
        {
            "input": [1, 4, 7],
            "output": True,
        },
        {
            "input": [2, 3],
            "output": False,
        },
        {
            "input": [4, 6],
            "output": True,
        },
    ]
    solution = Solution()

    for param in params:
        nums1 = param["input"]
        result = solution.uniformArray(nums1)
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
