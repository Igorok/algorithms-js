from typing import List
from json import dumps
import heapq
from collections import deque
import math


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.length = 4 * self.n
        self.array = [0] * self.length

        self._build(0, 0, self.n - 1)

    def _build(self, id: int, left: int, right: int):
        if left == right:
            self.array[id] = self.nums[left]
            return self.array[id]

        lId = 1 + id * 2
        rId = 2 + id * 2
        middle = (left + right) // 2

        lSum = self._build(lId, left, middle)
        rSum = self._build(rId, middle + 1, right)

        self.array[id] = lSum + rSum

        return self.array[id]

    def _get(self, id: int, left: int, right: int, start: int, end: int) -> int:
        if left > end:
            return 0
        if right < start:
            return 0
        if start <= left and end >= right:
            return self.array[id]

        lId = 1 + id * 2
        rId = 2 + id * 2
        middle = (left + right) // 2

        lSum: int = self._get(lId, left, middle, start, end)
        rSum: int = self._get(rId, middle + 1, right, start, end)

        return lSum + rSum

    def get(self, start: int, end: int):
        return self._get(0, 0, self.n - 1, start, end)

    def _update(self, id: int, left: int, right: int, index: int, diff: int):
        if index < left:
            return 0
        if index > right:
            return 0

        self.array[id] += diff

        if left == right:
            return

        lId = 1 + id * 2
        rId = 2 + id * 2
        middle = (left + right) // 2

        self._update(lId, left, middle, index, diff)
        self._update(rId, middle + 1, right, index, diff)

    def update(self, id: int, val: int):
        diff = val - self.nums[id]
        self.nums[id] = val
        return self._update(0, 0, self.n - 1, id, diff)


class Solution:
    def _getNumbers(self, n: int, edges: List[List[int]]):
        adj: List[List[List[int]]] = [[] for _ in range(n + 1)]
        for s, e, w in edges:
            adj[s].append([e, w])
            adj[e].append([s, w])

        def dfs(node: int, parent: int):
            for nei, weight in adj[node]:
                if nei == parent:
                    continue

                self.parents[nei] = node

                self.inOut[nei][0] = len(self.arr)
                self.arr.append(weight)
                dfs(nei, node)
                self.inOut[nei][1] = len(self.arr)
                self.arr.append(-weight)

        self.arr.append(0)
        dfs(1, 1)
        self.inOut[1][1] = len(self.arr)
        self.arr.append(0)

    def getChildAndParent(self, id1: int, id2: int):
        return [id1, id2] if self.parents[id1] == id2 else [id2, id1]

    def treeQueries(
        self, n: int, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        self.parents: List[List[int]] = [0] * (n + 1)
        self.parents[1] = 1
        self.inOut: List[List[int]] = [[0, 0] for _ in range(n + 1)]
        self.arr: List[int] = []

        self._getNumbers(n, edges)

        segmentTree = SegmentTree(self.arr)

        res = []
        for query in queries:
            if query[0] == 1:
                child, parent = self.getChildAndParent(query[1], query[2])

                chlIn = self.inOut[child][0]
                chlOut = self.inOut[child][1]

                segmentTree.update(chlIn, query[3])
                segmentTree.update(chlOut, -query[3])
                # print("upd")
            else:
                child = query[1]
                chlIn = self.inOut[child][0]
                val = segmentTree.get(0, chlIn)
                res.append(val)

        return res


"""

   0
   1
2 4  8
6 5 7 10
3   9



[0, 7, -7, 0]
[0, 7], [-7, 0]
[0], [7], [-7], [0]

"""


def test():
    params = [
        {
            "input": [
                3,
                [[1, 2, 2], [1, 3, 3]],
                [[2, 2], [2, 3], [1, 1, 2, 4], [2, 3]],
            ],
            "output": [2, 3, 3],
        },
        {
            "input": [2, [[1, 2, 7]], [[2, 2], [1, 1, 2, 4], [2, 2]]],
            "output": [7, 4],
        },
        {
            "input": [
                3,
                [[1, 2, 2], [1, 3, 4]],
                [[2, 1], [2, 3], [1, 1, 3, 7], [2, 2], [2, 3]],
            ],
            "output": [0, 4, 2, 7],
        },
        {
            "input": [
                4,
                [[1, 2, 2], [2, 3, 1], [3, 4, 5]],
                [[2, 4], [2, 3], [1, 2, 3, 3], [2, 2], [2, 3]],
            ],
            "output": [8, 3, 2, 5],
        },
    ]
    solution = Solution()

    for param in params:
        n, edges, queries = param["input"]
        result = solution.treeQueries(n, edges, queries)
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
