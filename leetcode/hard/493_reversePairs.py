import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List

"""
Today I decide to try a new issue instead of already completed in leetcode - "493. Reverse Pairs".
But look like my solution is not optimal

"""


class Solution_0:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0

        def search(arr, val):
            id = -1

            start = 0
            end = len(arr) - 1

            while start <= end:
                middle = (start + end) // 2

                if val > 2 * arr[middle]:
                    id = middle
                    start = middle + 1
                else:
                    end = middle - 1

            return id

        def rec(arr):
            nonlocal res

            if len(arr) < 2:
                return arr

            localRes = 0
            m = len(arr) // 2
            left = rec(arr[:m])
            right = rec(arr[m:])

            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    id = search(right, left[i])
                    if id != -1:
                        localRes += id + 1
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                id = search(right, left[i])
                if id != -1:
                    localRes += id + 1
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            res += localRes

            return merged

        rec(nums)

        return res


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0

        def rec(arr):
            nonlocal res

            if len(arr) < 2:
                return arr

            m = len(arr) // 2
            left = rec(arr[:m])
            right = rec(arr[m:])

            localRes = 0
            rightId = 0
            for num in left:
                while rightId < len(right) and num > right[rightId] * 2:
                    rightId += 1

                if rightId - 1 > -1 and num > right[rightId - 1] * 2:
                    localRes += rightId

            # j = 0
            # for i in range(len(left)):
            #     while j < len(right) and left[i] > 2 * right[j]:
            #         j += 1
            #     self.res += j

            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            while i < len(left):
                merged.append(left[i])
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            res += localRes

            return merged

        rec(nums)

        return res


"""
[1, 3, 2, 3, 1]

I think this is easy - "493. Reverse Pairs"
But look like not. I can implement merge sort and I will move values from right to left.

1, 3
1, 2, 3


"""


def test():
    params = [
        {
            "input": [1, 3, 2, 3, 1],
            "output": 2,
        },
        {
            "input": [2, 4, 3, 5, 1],
            "output": 3,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.reversePairs(nums)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
