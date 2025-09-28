from typing import List
import json
from collections import deque
import math


class SegemntTree:
    def __init__(self, nums):
        self.n = len(nums)
        length = 4 * self.n

        self.nums = nums
        self.array = [0] * length
        self.buildTree(0, 0, self.n - 1)

    def buildTree(self, id: int, start: int, end: int) -> int:
        if start == end:
            self.array[id] = self.nums[start]
            return self.array[id]

        lId = 1 + id * 2
        rId = 2 + id * 2
        middle = (start + end) // 2

        left = self.buildTree(lId, start, middle)
        right = self.buildTree(rId, middle + 1, end)
        self.array[id] = left + right
        return self.array[id]

    def _get(self, id, s, e, start, end):
        if s >= start and e <= end:
            return self.array[id]

        if e < start or s > end:
            return 0

        middle = (s + e) // 2
        lId = 1 + id * 2
        rId = 2 + id * 2

        left = self._get(lId, s, middle, start, end)
        right = self._get(rId, middle + 1, e, start, end)

        return left + right

    def get(self, start: int, end: int):
        s = 0
        e = self.n - 1
        return self._get(0, s, e, start, end)

    def _update(self, id, start, end, i, diff):
        if start > i:
            return
        if end < i:
            return

        self.array[id] += diff

        if start == end:
            return

        middle = (start + end) // 2
        lId = 1 + 2 * id
        rId = 2 + 2 * id

        self._update(lId, start, middle, i, diff)
        self._update(rId, middle + 1, end, i, diff)

        return

    def update(self, id: int, val: int):
        diff: int = val - self.nums[id]
        self.nums[id] = val

        return self._update(0, 0, self.n - 1, id, diff)


"""
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5], [6, 7, 8, 9]
[1, 2, 3], [4, 5], [6, 7], [8, 9]
[1, 2], [3], [4], [5], [6], [7], [8], [9]
[1], [2], [3], [4], [5], [6], [7], [8], [9]




"""


class NumArray:
    def __init__(self, nums: List[int]):
        self.segemntTree = SegemntTree(nums)

    def update(self, index: int, val: int) -> None:
        self.segemntTree.update(index, val)
        return

    def sumRange(self, left: int, right: int) -> int:
        return self.segemntTree.get(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


def test():
    params = [
        # {
        #     "input": [
        #         ["NumArray", "sumRange", "update", "sumRange"],
        #         [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]],
        #     ],
        #     "output": [None, 9, None, 8],
        # },
        {
            "input": [
                ["NumArray", "update", "sumRange", "sumRange", "update", "sumRange"],
                [[[9, -8]], [0, 3], [1, 1], [0, 1], [1, -3], [0, 1]],
            ],
            "output": [None, 9, None, 8, 1, 1],
        },
    ]

    for param in params:
        commands, data = param["input"]
        numArray = NumArray(*data[0])

        for i in range(1, len(commands)):
            result = None
            if commands[i] == "update":
                result = numArray.update(*data[i])
            if commands[i] == "sumRange":
                result = numArray.sumRange(*data[i])

            correct = json.dumps(result) == json.dumps(param["output"][i])

            msg = "SUCCESS" if correct else "ERROR"
            msg += "\n"
            msg += "input " + commands[i] + " " + json.dumps(data[i]) + "\n"
            msg += "output " + json.dumps(param["output"][i]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

            print(msg)


if __name__ == "__main__":
    test()
