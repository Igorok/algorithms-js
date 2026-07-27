import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        N = len(firstList)
        M = len(secondList)

        if N == 0 or M == 0:
            return []

        i = 0
        j = 0
        res = []

        while i < N and j < M:
            if firstList[i][0] > secondList[j][1]:
                j += 1
                continue

            if firstList[i][1] < secondList[j][0]:
                i += 1
                continue

            res.append(
                (
                    max(firstList[i][0], secondList[j][0]),
                    min(firstList[i][1], secondList[j][1]),
                )
            )

            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1

        return res


def test():
    params = [
        {
            "input": [
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
            ],
            "output": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        },
        {
            "input": [[[1, 3], [5, 9]], []],
            "output": [],
        },
    ]
    solution = Solution()

    for param in params:
        firstList, secondList = param["input"]
        result = solution.intervalIntersection(firstList, secondList)

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
