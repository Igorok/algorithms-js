import heapq
import json
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        stack = []
        for s, e in intervals:
            while stack and s <= stack[-1][0] and e >= stack[-1][1]:
                stack.pop()

            if stack and stack[-1][0] <= s and stack[-1][1] >= e:
                continue
            stack.append((s, e))

        return len(stack)


def test():
    params = [
        {
            "input": [[1, 4], [3, 6], [2, 8]],
            "output": 2,
        },
        {
            "input": [[1, 4], [2, 3]],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        intervals = param["input"]
        result = solution.removeCoveredIntervals(intervals)
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
