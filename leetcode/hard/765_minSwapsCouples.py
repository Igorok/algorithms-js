import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List

"""

"""


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        N = len(row)
        currId = [0] * N
        for i in range(N):
            currId[row[i]] = i

        res = 0
        for i in range(0, N, 2):
            a, b = row[i], row[i + 1]

            if (min(a, b) % 2) == 0 and max(a, b) - min(a, b) == 1:
                continue

            nei = a + 1 if (a % 2) == 0 else a - 1
            neiId = currId[nei]

            currId[nei] = i + 1
            row[i + 1] = nei

            row[neiId] = b
            currId[b] = neiId

            res += 1

        return res


"""
5, 2, 4, 1, 0, 3
5, 4, 2, 1, 0, 3
5, 4, 2, 3, 0, 1

5_2, 4_1, 0_3

"""


def test():
    params = [
        {
            "input": [0, 2, 1, 3],
            "output": 1,
        },
        {
            "input": [3, 2, 0, 1],
            "output": 0,
        },
        {
            "input": [3, 2, 0, 1, 4, 5],
            "output": 0,
        },
        {
            "input": [5, 2, 4, 1, 0, 3],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        row = param["input"]
        result = solution.minSwapsCouples(row)

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
