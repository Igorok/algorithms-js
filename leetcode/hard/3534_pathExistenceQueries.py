import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        labelsByNode = [0] * n

        return []


def test():
    params = [
        {
            "input": [5, [1, 8, 3, 4, 2], 3, [[0, 3], [2, 4]]],
            "output": [1, 1],
        },
        {
            "input": [5, [5, 3, 1, 9, 10], 2, [[0, 1], [0, 2], [2, 3], [4, 3]]],
            "output": [1, 2, -1, 1],
        },
        {
            "input": [3, [3, 6, 1], 1, [[0, 0], [0, 1], [1, 2]]],
            "output": [0, -1, -1],
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
