import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from operator import countOf
from typing import List


class Solution_0:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            count = 0
            for j in range(i, N):
                if nums[j] == target:
                    count += 1
                if count > (j - i + 1) // 2:
                    res += 1

        return res


class SegmentTree:
    def __init__(self, N):
        self.N = N
        self.length = 4 * ((self.N + 2) * 2)
        self.tree = [0] * self.length

    def _increase(self, left, right, treeId, val):
        if val > right or val < left:
            return

        self.tree[treeId] += 1

        if left == right:
            return

        middle = (left + right) // 2
        leftChild = treeId * 2 + 1
        rightChild = treeId * 2 + 2

        self._increase(left, middle, leftChild, val)
        self._increase(middle + 1, right, rightChild, val)

    def increase(self, val):
        # convert for negative
        localVal = val + self.N
        self._increase(0, self.N * 2, 0, localVal)

    def _getCount(self, left, right, treeId, valLeft, valRight):
        if valRight < left or valLeft > right:
            return 0

        if left == right:
            return self.tree[treeId]

        if left >= valLeft and right <= valRight:
            return self.tree[treeId]

        res = 0

        middle = (left + right) // 2
        leftChild = treeId * 2 + 1
        rightChild = treeId * 2 + 2

        res += self._getCount(left, middle, leftChild, valLeft, valRight)
        res += self._getCount(middle + 1, right, rightChild, valLeft, valRight)

        return res

    def getCount(self, val):
        localVal = val + self.N
        return self._getCount(0, self.N * 2, 0, 0, localVal)


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        sTree = SegmentTree(N)
        sTree.increase(0)

        res = 0
        count = 0

        for i in range(N):
            val = 1 if nums[i] == target else -1
            count += val
            cnt = sTree.getCount(count - 1)

            res += cnt
            sTree.increase(count)

        return res


"""
"input": [[1, 2, 2, 3], 2],
"output": 5,

1, 2, 2, 3, 2, 4
-1 1  1 -1  1 -1
-1 0  1  0  1  0
0  1  2  2  3  3

1   1   1   1   1   1   2   2   1   1   1   1
-1 -2  -3  -4  -5  -6  -5  -4  -5  -6  -7  -8

Where target is major? In the subarray which prefix sum > 0.
How can I get the sum of subarray? Sum = p[j] - p[i-1]:
p[j] - p[i-1] > 0
What this formula can say for me?
p[j] > p[i-1]
I know all values less that p[j], I know count of subarrays.

"""


def test():
    params = [
        {
            "input": [[1, 2, 2, 3], 2],
            "output": 5,
        },
        {
            "input": [[1, 1, 1, 1], 1],
            "output": 10,
        },
        {
            "input": [[1, 2, 3], 4],
            "output": 0,
        },
        {
            "input": [[1, 2, 2, 3, 2, 4], 2],
            "output": 10,
        },
    ]
    solution = Solution()

    for param in params:
        nums, target = param["input"]
        result = solution.countMajoritySubarrays(nums, target)
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
