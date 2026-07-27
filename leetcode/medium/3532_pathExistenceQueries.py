import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:

        label = 0
        labels = [0] * n

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                labels[i] = labels[i - 1]
                continue
            label += 1
            labels[i] = label

        m = len(queries)
        res = [False] * m

        for i in range(m):
            s, e = queries[i]
            res[i] = labels[s] == labels[e]

        return res


def test():
    params = [
        {
            "input": [2, [1, 3], 1, [[0, 0], [0, 1]]],
            "output": [True, False],
        },
        {
            "input": [4, [2, 5, 6, 8], 2, [[0, 1], [0, 2], [1, 3], [2, 3]]],
            "output": [False, False, True, True],
        },
    ]
    solution = Solution()

    for param in params:
        n, nums, maxDiff, queries = param["input"]
        result = solution.pathExistenceQueries(n, nums, maxDiff, queries)

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
